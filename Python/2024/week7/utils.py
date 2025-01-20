"""
Name: utils.py
Author: Mikhail Zubko
Purpose: A utility module with commonly used functions
"""

from random import randint
from math import cos, sin, radians

# constants
PHI = 0.5 + 0.5 * 5**0.5  # phi - the golden ratio


def get_title(title: str) -> str:
    """
    Take str as input, return a decorated str
    """
    txt_len = len(title)
    line = "+--" + "-" * txt_len + "--+\n"
    title = f"|  {title}  |\n"
    return line + title + line


def get_float(prompt: str):
    """
    Get a float number from the user, check the input
    Return float if it's correct, or ask again
    Return False if no input.
    """
    while True:
        inp = input(prompt).strip().replace(",", "")
        if not inp:  # exit if no input
            return None
        if inp.replace(".", "", 1).isdigit():  # clean and check user's input
            try:  # in case of really unusual inputs
                return float(inp)
            except ValueError:
                print("Looks like you entered something really weird")
        print(f"You entered: {inp} which is not a number")
        print("Let's try again.")


def random_color(min: int = 0, max: int = 255) -> tuple[int, int, int]:
    """
    RGB color randomizer
    Return rgb as (int, int, int) in range from min to max
    Low limit: 0
    High limit: 255
    """
    if min < 0 or min >= max:
        min = 0
    if max > 255 or max < 1:
        max = 255
    r = randint(min, max)
    g = randint(min, max)
    b = randint(min, max)
    return r, g, b


def polar_to_cartesian(r: float, theta: float) -> tuple[float, float]:
    """
    Convert polar coordinates (r, theta) to Cartesian (x, y).
    theta - angle in degrees
    """
    x = r * cos(radians(theta))
    y = r * sin(radians(theta))
    return x, y


if __name__ == "__main__":
    # Tests here
    print(PHI)
    print(get_title("Hello, World!"))
    print(get_float("Enter a number: "))
    print(random_color(15, 225))
    print(polar_to_cartesian(5.5, 111.8))
