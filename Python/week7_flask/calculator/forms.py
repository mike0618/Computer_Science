from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, SelectField
from wtforms.validators import DataRequired


# Define WTForm
class CalcForm(FlaskForm):
    num1 = DecimalField("First number", validators=[DataRequired()])
    num2 = DecimalField("Second number", validators=[DataRequired()])
    op = SelectField(
        "Operation",
        choices=[("+", "Sum"), ("-", "Subtract"), ("*", "Multiply"), ("/", "Divide")],
    )
    calc = SubmitField("Calculate")
