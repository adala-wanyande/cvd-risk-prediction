## Cardiovascular Disease (CVD) Risk Prediction Using Multi-Layer Perceptron (MLP)

### Project Description

This project aims to predict cardiovascular disease (CVD) using an advanced Machine Learning (ML) model. CVD is a leading global cause of mortality, demanding innovative diagnostic approaches. The project proposes an Artificial Neural Network (ANN) model for enhanced accuracy, overcoming limitations of traditional methods like ECG. The ANN model surpasses conventional approaches, achieving significant accuracy improvements. Through feature selection and ANN-based training, the model's performance is evaluated using various metrics. The objective is to establish a robust ML model for swift and reliable CVD risk predictions, ushering in a new era of predictive healthcare.

### Key Features

* 94% accuracy for the dataset it uses, much higher than other projects using the same dataset
* Implements neural networks with MLP as opposed to other classical ML approaches
* Implements an API, web, and mobile app to accompany the ML model
* Users can find out their risk of suffering from CVD based on a few parameters

### Deployment Platform

Heroku

### Installation Instructions

Still in the process of implementing the API

### Dependencies

This project relies on several dependencies, including:

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- imbalanced-learn (imblearn)
- pickle
- IPython
- and more...

### API Documentation

Still in the process of implementing the API

### Model Information

The model is a Multi-Layer Perceptron (MLP) neural network. It has 94% accuracy for the dataset it uses, which is much higher than other projects using the same dataset.

## Example requests and responses

**Request**


GET /predict?age=35&sex=male&cholesterol=200&blood_pressure=130/80&smoker=yes
Use code with caution. Learn more
Response

JSON
{
  "prediction": "high"
}


This response indicates that the user has a high risk of developing CVD.

## How to use the project

To use the project, you can either use the API, web app, or mobile app.

### To use the API:

1. Send a GET request to the `/predict` endpoint with the following parameters:
    * `age`: The user's age in years.
    * `sex`: The user's sex (male or female).
    * `cholesterol`: The user's cholesterol level in mg/dL.
    * `blood_pressure`: The user's blood pressure in mmHg (systolic/diastolic).
    * `smoker`: Whether the user is a smoker (yes or no).

2. The API will return a JSON response with the following fields:
    * `prediction`: The user's risk of developing CVD (low, medium, or high).

### To use the web app:

1. Visit the web app URL.
2. Enter the user's age, sex, cholesterol level, blood pressure, and smoking status.
3. Click the "Predict" button.
4. The web app will display the user's risk of developing CVD (low, medium, or high).

### To use the mobile app:

1. Download and install the mobile app.
2. Open the mobile app and enter the user's age, sex, cholesterol level, blood pressure, and smoking status.
3. Tap the "Predict" button.
4. The mobile app will display the user's risk of developing CVD (low, medium, or high).