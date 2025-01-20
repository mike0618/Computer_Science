"""
Name: leap_year.py
Author: Mikhail Zubko
Created: 08/25/2024
Purpose: Check if a given year is leap.
"""


# TODO: Print a creative title for our program
def print_title():
    title = "|  Leap Year  |"
    line = "-" * len(title)  # create a line the same length as the title
    print(f"{line}\n{title}\n{line}")  # print the title between 2 horizontal lines


# TODO: User input handle function
def get_numbers(msg: str):
    # get user's input replacing possible commas in case of 123,456.78 number notation.
    user_input = input(msg).replace(",", "")
    # check if user's input is proper
    if user_input.isdigit():
        return int(user_input)
    return False  # ...if it's not False is here explicitly for readability.


# TODO: Main function
def main():
    print_title()  # Print our title once in the beginning
    msg1 = "\nEnter a year: "
    while True:  # here's a magic eternal loop to have some fun ;)
        # TODO: Get user input
        year = get_numbers(msg1)
        if not year:
            # if we didn't get a proper input, the loop will be broken by return
            print("Good bye!")
            return False
        # TODO: Check a year
        # A leap year is a multiple of 4, except for years evenly divisible by 100 but not by 400.
        # thus, a year evenly divisible by 400 is always leap, and the rest years
        # that evenly divisible by 4 but not divisible by 100 are leap too.
        if not year % 400 or (year % 100 and not year % 4):
            print(f"{year} is a Leap year.")
        else:
            print(f"{year} is NOT a Leap year.")


if __name__ == "__main__":
    # Here, if this file's been started directly, the main function will be started.
    main()
