from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.joblib")   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/check')
def check():
    return render_template('check_quality.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
         
        features = [
            float(request.form['fixed_acidity']),
            float(request.form['volatile_acidity']),
            float(request.form['citric_acid']),
            float(request.form['chlorides']),
            float(request.form['total_sulfur_dioxide']),
            float(request.form['sulphates']),
            float(request.form['alcohol'])
        ]
        prediction = model.predict([features])[0]
        return f"<h2>Predicted Wine Quality: {prediction}</h2><a href='/check'>Try Again</a>"
    except Exception as e:
        return f"<h2>Error: {e}</h2><a href='/check'>Try Again</a>"

if __name__ == '__main__':
    app.run(debug=True)
