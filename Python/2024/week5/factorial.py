# I already did a loop in the previous programm
# there's a factorial function in the math module, let's use it now.
from math import factorial as f


# here's aur function
def factorial(n: int) -> int:
    return f(n)


if __name__ == "__main__":
    print("This module is not supposed to be run directly, please use main.py")
