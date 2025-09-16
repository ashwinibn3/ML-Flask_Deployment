# ML-Flask-Deployment
Fitness Predictor – Flask Deployment Demo

This is a small end-to-end project where I trained a regression model and deployed it with Flask as a simple web app. The idea is to take a model beyond the Jupyter notebook and make it usable through a browser form.

What it does

Uses the classic Linnerud dataset from scikit-learn (20 samples).

Inputs: number of chin-ups, sit-ups, jumps a person can do.

Model: Multi-output Linear Regression (predicts 3 values at once).

Outputs: predicted Weight (kg), Waist (cm), and Pulse (bpm).

How it works

Training: Trained the regression model in a notebook, then saved it as model.pkl with joblib.

Flask backend: app.py loads the saved model and handles predictions.

Frontend: index.html is a very simple form where you enter exercise counts.

Run locally: Start the app with python app.py, open http://127.0.0.1:5000, enter numbers, and you’ll get predictions instantly.
Why I built this

I wanted to practice the deployment side of machine learning — not just training models but actually making them usable. Even though this is based on a toy dataset, it gave me hands-on experience with:

Model saving/loading

Building a Flask app with a prediction endpoint

Designing a basic HTML form for input/output

This project later became the base template I reused for other apps (like my Illness Prediction deployment).
