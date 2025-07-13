from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    N = int(request.form['N'])
    P = int(request.form['P'])
    K = int(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])

    features = [[N, P, K, temperature, humidity, ph, rainfall]]
    prediction = model.predict(features)[0]

    return render_template('predict.html', crop=prediction)

if __name__ == '__main__':
    app.run(debug=True)
