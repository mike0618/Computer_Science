from datetime import datetime
from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from jinja2 import runtime  # pip install flask_bootstrap
from forms import CalcForm
from secrets import token_hex

app = Flask("Calculator")  # create the app
app.secret_key = token_hex()  # a random session secret key to mitigate CSRF
Bootstrap(app)  # init bootstrap


@app.context_processor
def inject_year():
    """To use year on all project's pages'"""
    return {"year": datetime.now().year}


@app.route("/", methods=["GET", "POST"])  # the form uses POST on submit
def home():
    form = CalcForm()  # create a form object
    if not form.validate_on_submit():
        return render_template("index.html", form=form)
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
            return f"{num1 / num2}"
    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
