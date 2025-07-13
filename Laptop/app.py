from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs from form as integers/floats (no encoding needed, user enters raw numbers)
        features = [
            int(request.form['brand']),
            int(request.form['processor_1']),
            int(request.form['processor_2']),
            int(request.form['processor_3']),
            int(request.form['ram_gb']),
            int(request.form['ssd']),
            int(request.form['hdd']),
            int(request.form['graphic_card']),
            int(request.form['warranty']),
            int(request.form['Touchscreen']),
        ]

        prediction = model.predict([features])[0]
        output = round(prediction, 2)

        return render_template('predict.html', prediction_text=f"Estimated Laptop Price: ₹{output}")

    except Exception as e:
        return render_template('predict.html', prediction_text=f"Error: {str(e)}")

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
