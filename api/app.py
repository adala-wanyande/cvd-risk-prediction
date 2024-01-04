from flask import Flask, request, jsonify
import pickle
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load your model using pickle
with open('./models/mlp_model_rfe_94_v3.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the dataset
df = pd.read_csv('./data/dataset.csv')

# Small small data preprocessing
numerical = df.select_dtypes(include=['float64']).columns.sort_values()
categorical = df.select_dtypes(include=['object']).columns.sort_values()

cat_pipeline = make_pipeline(OneHotEncoder(handle_unknown='ignore', drop='first'))
num_pipeline = make_pipeline(
    FunctionTransformer(np.log1p, feature_names_out='one-to-one'),
    StandardScaler()
)

## Age Category Pipeline
agecat_pipeline = make_pipeline(
    OrdinalEncoder()
)

## General Health Pipeline
genhealth_pipeline = make_pipeline(
    OrdinalEncoder(categories=[['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']])
)

## Checkup Pipeline
checkup_pipeline = make_pipeline(
    OrdinalEncoder(categories=[['Within the past year', 'Within the past 2 years', 'Within the past 5 years',
                                '5 or more years ago', 'Never']])
)

## Setting each column to the pipeline where they will be used
num_pipe_col = numerical

cat_pipe_col = ['Arthritis', 'Depression', 'Diabetes',
                'Exercise', 'Other_Cancer', 'Sex',
                'Skin_Cancer', 'Smoking_History']

## Combining all the pipelines and creating a main pipeline to enter all the data
preprocessing = ColumnTransformer([
    ('Categorical', cat_pipeline, cat_pipe_col),
    ('Age_Category', agecat_pipeline, ['Age_Category']),
    ('Checkup', checkup_pipeline, ['Checkup']),
    ('Gen_health', genhealth_pipeline, ['General_Health']),
    ('Numerical', num_pipeline, num_pipe_col),
], remainder='passthrough')

X_train = df.drop('Heart_Disease', axis=1)  # Assuming 'Heart_Disease' is your target variable
y_train = df['Heart_Disease']
preprocessing.fit(X_train, y_train)

@app.route('/', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.get_json()

        # Ensure that the required fields are present in the request
        if 'features' not in data:
            return jsonify({'error': 'Missing features field in the request'}), 400

        # Extract features from the request
        features = pd.DataFrame(data['features'])

        # Preprocess the input
        preprocessed_input = preprocessing.transform(features)  # Wrap features in a list

        # Make predictions using the loaded model
        prediction = model.predict(preprocessed_input)

        # Return the prediction as JSON
        return jsonify({'prediction': int(prediction[0])})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
