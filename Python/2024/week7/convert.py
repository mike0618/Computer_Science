"""
Name: convert.py
Author: Mikhail Zubko
Purpose: A module with converting functions
"""


def cm_to_inches(input: float) -> str:
    # Pass float user input to function
    return f"{input} centimeters is {input / 2.54:,.2f} inches."


def inches_to_cm(input: float) -> str:
    return f"{input} inches is {input * 2.54:,.2f} centimeters."


def km_to_miles(input: float) -> str:
    return f"{input} kilometers is {input / 1.609344:,.2f} miles."


def miles_to_km(input: float) -> str:
    return f"{input} miles is {input * 1.609344:,.2f} kilometers."
