"""
Name: circle.py
Author: Mikhail Zubko
Created: 10/22/2024
Purpose: Calculate the diameter, area and Circumference of a circle or a sector
"""

from math import pi


# TODO: Define CircleCalculator class
class CircleCalculator:
    def __init__(self) -> None:
        # TODO: Print a creative title for our program
        self.title = (
            "|                  Circe's Circle/Sector Calculator                 |"
        )
        self.subtitle = (
            "| Calculate the Diameter, Area and Circumference of a Circle/Sector |"
        )
        self.line = "-" * len(self.title)  # create a line the same length as the title
        self.radius = 0
        self.angle_units = "d"
        self.angle = 2 * pi
        # print the title between 2 horizontal lines
        print(f"{self.line}\n{self.title}\n{self.subtitle}\n{self.line}\n")

    # TODO: Get and check user's radius input, cast to float
    def set_radius(self, radius_input=None):
        if not radius_input:
            msg = "Enter the Radius of a Circle/Sector (nothing to exit): "
            radius_input = input(msg)
        # get user's input replacing possible commas in case of 123,456.78 number notation.
        radius_input = radius_input.replace(",", "").strip()
        # if the radius input is not a proper "floatable" number, return False
        if not radius_input.replace(".", "", 1).isdigit():
            return False
        self.radius = float(radius_input)
        return True

    # TODO: Get user's angle units input
    def set_units(self, units=None):
        if not units:
            msg = "\nEnter 'p' for PI, 'r' for radians, degrees is default: "
            units = input(msg).lower()
        if units and units[0] in ("p", "r", "d"):
            self.angle_units = units

    # TODO: Get and check user's angle input, cast to float
    def set_angle(self, angle_input=None):
        if angle_input is None:
            msg = "\nEnter the Angle of a Sector, nothing for a full circle: "
            angle_input = input(msg)
        angle_input = angle_input.replace(",", "").strip()
        if not angle_input or angle_input == "0":
            return False
        # check if input is correct
        elif angle_input.replace(".", "", 1).isdigit():
            match self.angle_units:
                case "d":  # if angle input in degrees, it will be converted to radians
                    self.angle = float(angle_input) * pi / 180
                case "p":
                    self.angle = float(angle_input) * pi
                case "r":
                    self.angle = float(angle_input)

    # TODO: Calculate Diameter
    def calc_diameter(self):
        return self.radius * 2

    # TODO: Calculate Area
    def calc_area(self):
        return self.radius**2 * self.angle / 2

    # TODO: Calculate Circumference
    def calc_ark(self):
        return self.radius * self.angle

    # TODO: __repr__ Method to concatenate results as a string and return to
    # main to be displayed
    def __repr__(self) -> str:
        return f"{self.line}\nYour inputs:\n     Radius: {self.radius:,.2f}\n      Angle: {self.angle:,.2f}\n{self.line}\n   Diameter: {self.calc_diameter():,.2f}\n       Area: {self.calc_area():,.2f}\nCircumference or\n Arc length: {self.calc_ark():,.2f}\n{self.line}\n"


if __name__ == "__main__":
    calc = CircleCalculator()
    while True:
        if not calc.set_radius():
            break
        calc.set_units()
        calc.set_angle()
        print(calc)
