"""
Name: square_calculator.py
Author: Mikhail Zubko
Created: 08/21/2024
Purpose: Calculate the area and perimeter of a square
"""


# TODO: Print a creative title for our program
def print_title():
    title = "|    Susie's Square Calculator   |"
    line = "-" * len(title)  # create a line the same length as the title
    print(f"{line}\n{title}\n{line}")  # print the title between 2 horizontal lines


# TODO: Get side and length from user, cast to float
def get_length():
    msg = "Enter the length of a side (0 or a letter to exit): "
    # get user's input replacing possible commas in case of 123,456.78 number notation.
    user_input = input(msg).replace(",", "")
    # check if user's input is a proper "floatable" number...
    if user_input.replace(".", "", 1).isdigit():
        return float(user_input)
    return False  # ...if it's not False is here explicitly for readability.


# TODO: Display results
def main():
    print_title()  # Print our title once in the beginning
    while True:  # here's a magic eternal loop to have some fun ;)
        side = get_length()
        if not side:
            # if we didn't get a side length, the loop will be broken by return
            print("Good bye!")
            return False
        # TODO: Calculate area
        print(f"     Area: {side * side:.2f}")  # :.2f to format string 2 digits after .
        # TODO: Calculate perimeter
        print(f"Perimeter: {side * 4:.2f}\n")


if __name__ == "__main__":
    # Here, if this file's been started directly, the main function will be started.
    main()
