from flask import Flask, request, render_template_string
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Customer Churn Prediction</title>
</head>
<body>
    <h2>Customer Churn Prediction</h2>
    <form method="post" action="/predict">
        Tenure: <input type="number" name="tenure"><br><br>
        Monthly Charges: <input type="number" name="monthly"><br><br>
        Total Charges: <input type="number" name="total"><br><br>
        Senior Citizen (0 or 1): <input type="number" name="senior"><br><br>
        <input type="submit" value="Predict">
    </form>

    {% if result %}
        <h3>Prediction Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_FORM)

@app.route("/predict", methods=["POST"])
def predict():
    tenure = int(request.form["tenure"])
    monthly = float(request.form["monthly"])
    total = float(request.form["total"])
    senior = int(request.form["senior"])

    features = np.array([[tenure, monthly, total, senior]])
    prediction = model.predict(features)[0]

    result = "Customer Will Churn ❌" if prediction == 1 else "Customer Will NOT Churn ✅"

    return render_template_string(HTML_FORM, result=result)

if __name__ == "__main__":
    app.run(debug=True)
