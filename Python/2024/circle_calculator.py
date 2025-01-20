"""
Name: circle_calculator.py
Author: Mikhail Zubko
Created: 08/23/2024
Purpose: Calculate the diameter, area and Circumference of a circle or a sector
"""

from math import pi


# TODO: Print a creative title for our program
title = "|                  Circe's Circle/Sector Calculator                 |"
subtitle = "| Calculate the Diameter, Area and Circumference of a Circle/Sector |"
line = "-" * len(title)  # create a line the same length as the title


def print_title():
    # print the title between 2 horizontal lines
    print(f"{line}\n{title}\n{subtitle}\n{line}\n")


# TODO: Get and check user's input, cast to float
def get_length():
    msg = "Enter the Radius of a Circle/Sector (nothing to exit): "
    # get user's input replacing possible commas in case of 123,456.78 number notation.
    radius_input = input(msg).replace(",", "")
    # if the radius input is not a proper "floatable" number, return False
    if not radius_input.replace(".", "", 1).isdigit():
        return False, 0
    radius = float(radius_input)
    angle = 2 * pi  # By default let's calculate for a full circle
    msg2 = "\nEnter the Angle of a Sector, for example:\n0.5p or 2.5 for radians, 202.5d for degrees, nothing for a full circle: "
    angle_input = input(msg2).replace(",", "")
    if angle_input == "p":
        angle = pi
    # check if input is correct
    elif angle_input.replace(".", "", 1).isdigit() or (
        angle_input
        and angle_input[-1] in ("d", "p")
        and angle_input[:-1].replace(".", "", 1).isdigit()
    ):
        match angle_input[-1]:
            case "d":  # if angle input in degrees, it will be converted to radians
                deg = float(angle_input[:-1])
                angle = deg * pi / 180
            case "p":
                angle = float(angle_input[:-1]) * pi
            case _:
                angle = float(angle_input)
    return radius, angle


# TODO: Display results
def main():
    print_title()  # Print our title once in the beginning
    while True:  # here's a magic eternal loop to have some fun ;)
        radius, angle = get_length()
        if not radius:
            # if we didn't get a radius length, the loop will be broken by return
            print("Good bye!")
            return False
        print(line)
        print("Your inputs:")
        print(f"     Radius: {radius:,.3f}")
        print(f"      Angle: {angle:,.3f} or {angle * 180 / pi:,.3f} degrees")
        print(line)
        # TODO: Calculate Diameter
        print(f"   Diameter: {radius * 2:,.3f}")
        # TODO: Calculate Area
        print(f"       Area: {radius * radius * angle / 2:,.3f}")
        # TODO: Calculate Circumference
        print(f"Circumference or\n Arc length: {radius * angle:,.3f}")
        print(line, "\n")


if __name__ == "__main__":
    # Here, if this file's been started directly, the main function will be started.
    main()
