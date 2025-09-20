from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    bmi_result = None
    if request.method == "POST":
        name = request.form["name"]
        age = int (request.form["age"])
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        bmi = round(weight / (height ** 2), 1)

        # classify BMI #
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        bmi_result = f"{name} ({age}) - BMI: {bmi} ({category})"

    return render_template("index.html", result=bmi_result)

if __name__ == "__main__":
    app.run(debug=True)

    