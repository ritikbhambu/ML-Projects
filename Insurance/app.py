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

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None

    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = int(request.form['smoker'])
        region = int(request.form['region'])

        features = [[age, sex, bmi, children, smoker, region]]
        prediction = model.predict(features)[0]

    return render_template('predict.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
