"""
Name: number_analysis.py
Author: Mikhail Zubko
Created: 09/05/2024
Purpose: Check a range of numbers.
"""

# TODO: Create a for loop
for n in range(1, 11):
    # TODO: Identify if number is odd or not
    if n % 2:
        print(f"Number {n} is odd.")
    else:
        print(f"Number {n} is even.")
    # TODO: Identify if number is a multiple of 3
    if not n % 3:
        print(f"Number {n} is a multiple of 3.")
