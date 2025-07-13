from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load("model.joblib")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("aboutus.html")

@app.route('/predict')
def form():
    return render_template("predict_salary.html")

@app.route('/predict_salary', methods=['POST'])
def predict_salary():
    try:
        experience = float(request.form['experience'])
        prediction = model.predict([[experience]])[0]
        return f"<h2 style='text-align:center;'>Predicted Salary: ${prediction:,.2f}</h2><p style='text-align:center;'><a href='/predict'>Predict Again</a></p>"
    except Exception as e:
        return f"<h2>Error: {e}</h2>"

if __name__ == '__main__':
    app.run(debug=True)
