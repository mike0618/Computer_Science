from datetime import datetime
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap  # pip install flask_bootstrap
from forms import CalcForm, ConvForm
from secrets import token_hex

app = Flask("Calculator")  # create the app
app.secret_key = token_hex()  # a random session secret key to mitigate CSRF
Bootstrap(app)  # init bootstrap
app.config["WTF_CSRF_TIME_LIMIT"] = None


@app.context_processor
def inject_year():
    """To use year on all project's pages'"""
    return {"year": datetime.now().year}


@app.route("/", methods=["GET", "POST"])  # the form uses POST on submit
def home():
    form = CalcForm()  # create a form object
    conv_form = ConvForm()  # create a form object
    if not form.validate_on_submit() or request.method == "GET":
        return render_template("index.html", form=form, conv_form=conv_form)
    # if form is validated, get data from it
    num1 = float(str(form.num1.data))
    num2 = float(str(form.num2.data))
    # match the operator and perform calculations
    match form.op.data:
        case "+":
            return f"{num1 + num2}"
        case "-":
            return f"{num1 - num2}"
        case "*":
            return f"{num1 * num2}"
        case "/":
            if num2:
                return f"{num1 / num2}"
            return "Zero division"
    return ""


@app.route("/calc", methods=["POST"])
def conv():
    form = ConvForm()
    if not form.validate_on_submit():
        return ""
    val = float(str(form.value.data))
    if form.method.data == "p":
        return f"{val * 2.20462:.3f} pounds."
    return f"{val / 2.20462:.3f} kilograms."


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
