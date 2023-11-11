from flask import Blueprint, request, jsonify
import pickle

predict = Blueprint("predict", __name__)

# Load the CVD risk prediction model
model = pickle.load(open("model.pkl", "rb"))

# Define the `/predict` route
@predict.route("/predict", methods=["POST"])
def predict_endpoint():
    # Get the input data from the request body
    input_data = request.get_json()

    # Make a prediction using the model
    prediction = model.predict(input_data)

    # Return the prediction to the client
    return jsonify({"prediction": prediction})