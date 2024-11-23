import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the trained model
model = tf.keras.models.load_model('banana_disease_model.keras')

# Image preprocessing function
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))  # Resize image
    img_array = image.img_to_array(img)  # Convert image to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Rescale the image
    return img_array

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Banana Disease Prediction API! Use POST /predict to upload an image."

@app.route('/predict', methods=['POST'])
def predict():
    # Check if an image file is sent in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save file temporarily for processing
    img_path = os.path.join('temp.jpg')
    file.save(img_path)

    # Preprocess image and make prediction
    img_array = preprocess_image(img_path)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)

    # Mapping class index to disease
    class_map = {0: 'Black Sigatoka', 1: 'Fusarium wilt', 2: 'Healthy'}
    predicted_label = class_map.get(predicted_class[0], 'Unknown')

    return jsonify({'prediction': predicted_label})

if __name__ == '__main__':
    app.run(debug=True)