from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, SelectField
from wtforms.validators import InputRequired


# Define WTForm
class CalcForm(FlaskForm):
    num1 = DecimalField("First number", validators=[InputRequired()])
    num2 = DecimalField("Second number", validators=[InputRequired()])
    op = SelectField(
        "Operation",
        choices=[("+", "Sum"), ("-", "Subtract"), ("*", "Multiply"), ("/", "Divide")],
    )
    calc = SubmitField("Calculate")


class ConvForm(FlaskForm):
    value = DecimalField("Value", validators=[InputRequired()])
    method = SelectField(
        "Conversion",
        choices=[("kg", "Pounds to Kilograms"), ("p", "Kilograms to Pounds")],
    )
    conv = SubmitField("Convert")
