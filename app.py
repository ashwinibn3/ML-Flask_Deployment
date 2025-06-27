from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs
        chinups = float(request.form['chinups'])
        situps = float(request.form['situps'])
        jumps = float(request.form['jumps'])

        # Format input for prediction
        input_data = np.array([[chinups, situps, jumps]])
        prediction = model.predict(input_data)[0]  # [weight, waist, pulse]

        # Return result to HTML
        return render_template('index.html', result={
            'weight': round(prediction[0], 2),
            'waist': round(prediction[1], 2),
            'pulse': round(prediction[2], 2)
        })

    except:
        return render_template('index.html', error="Invalid input. Please enter numbers.")

if __name__ == '__main__':
    app.run(debug=True)
