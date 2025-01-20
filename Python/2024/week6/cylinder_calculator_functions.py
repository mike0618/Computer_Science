"""
Name: cylinder_calculator_functions.py
Author: Mikhail Zubko
Created: 09/25/24
Purpose: Calculate the surface area and volume of a cylinder
"""

# TODO: Import math module
from math import pi


# TODO: program_title() Print creative program title
title = "|          Calypso's Master Cylinder Calculator         |"
subtt = "|  Calculate the surface area and volume of a cylinder  |"
line = "-" * len(title)


def program_title():
    print(line)
    print(title)
    print(subtt)


# TODO: get_radius() Get user input for radius as float
def get_radius() -> float:
    return float(input("Enter radius: "))


# TODO: get_height() Get user input for height as float
def get_height() -> float:
    return float(input("Enter height: "))


# TODO: get_volume() Calculate volume of cylinder Math formula: v = πr2h
def get_volume(r: float, h: float) -> float:
    return h * pi * r**2


# TODO: get_surface_area() Calculate surface area of cylinder Math formula: A = 2πrh + 2πr2
def get_surface_area(r: float, h: float) -> float:
    return 2 * pi * r * h + 2 * pi * r**2


def display_results(r: float, h: float, v: float, a: float):
    print(line)
    # TODO: Echo user input
    print(" You entered:")
    print(f"      Radius: {r}")
    print(f"      Height: {h}")
    # TODO: Display results
    # Use f-strings to format float to 2 decimal places
    # use comma (,) as a 1,000’s separator
    print(line)
    print(f"      Volume: {v:,.2f}")
    print(f"Surface Area: {a:,.2f}")


def main():
    while True:
        print(line)
        try:
            radius = get_radius()
            height = get_height()
            break  # exit the loop if input is correct
        except ValueError:  # catch wrong user input and repeat the question
            print("Wrong input: enter a whole or float number.")
            continue
    volume = get_volume(radius, height)
    area = get_surface_area(radius, height)
    display_results(radius, height, volume, area)


if __name__ == "__main__":
    program_title()
    # TODO: Ask user to run program again
    while True:
        main()
        if input("Again? (y/N): ").lower() != "y":
            break  # if answer is not y or Y, exit the loop, by default exit.
