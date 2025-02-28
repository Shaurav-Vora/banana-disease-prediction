# Banana Disease Prediction

This project predicts banana leaf diseases using a deep learning model. Users can upload an image of a banana leaf, and will return a prediction indicating whether the leaf is healthy or affected by Black Sigatoka and Fusarium wilt.

---

## Repository Structure

- **Backend/**: Contains the Flask API for image processing and predictions.
- **Frontend/**: Contains the React application for user interaction.

---

# Clone the repository
```bash
git clone git@github.com:Shaurav-Vora/banana-disease-prediction.git
cd banana-disease-prediction
```
# Backend setup
## Requirements
- Python 3.7 or higher
- Required Python packages:
  - Flask
  - Flask-CORS
  - TensorFlow
  - NumPy

You can install the dependencies using:
```bash
pip install -r requirements.txt
```

## Start backend server
```bash
cd Backend
python app.py
```
# Frontend Setup

The frontend of this project is built using React and styled with Tailwind CSS. Follow these steps to set up and run the frontend locally.

---

### Prerequisites

Ensure the following are installed on your system:
- **Node.js**: Version 16 or higher (Download it from [Node.js Official Website](https://nodejs.org/)).
- **npm**: Comes bundled with Node.js (or alternatively, use `yarn`).

---

## Start frontend server
```bash
cd ../Frontend
npm install
npm start
```

# Accessing the application
- Ensure both the backend and frontend servers are running.
- Open your browser and navigate to http://localhost:3000 to use the application.

# Notes
- **API Endpoint:** The React app communicates with the backend at http://127.0.0.1:5000/predict. Update this URL in the React code if your backend is hosted elsewhere.

# Troubleshooting
- Ensure all dependencies are installed correctly.
- Verify the backend server is running at the specified address before starting the frontend.
- Use a different port for the frontend if port 3000 is occupied
