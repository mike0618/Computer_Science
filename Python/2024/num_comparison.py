"""
Name: num_comparison.py
Author: Mikhail Zubko
Created: 08/25/2024
Purpose: Compare 2 numbers
"""


# TODO: Print a creative title for our program
def print_title():
    title = "|  Number Comparison  |"
    line = "-" * len(title)  # create a line the same length as the title
    print(f"{line}\n{title}\n{line}")  # print the title between 2 horizontal lines


# TODO: User input handle function
def get_numbers(msg: str):
    # get user's input replacing possible commas in case of 123,456.78 number notation.
    user_input = input(msg).replace(",", "")
    # check if user's input is a proper "floatable" number...
    if user_input.replace(".", "", 1).isdigit():
        return float(user_input)
    return False  # ...if it's not False is here explicitly for readability.


# TODO: Main function
def main():
    print_title()  # Print our title once in the beginning
    msg1 = "\nEnter the 1st number: "
    msg2 = "Enter the 2nd number: "
    while True:  # here's a magic eternal loop to have some fun ;)
        # TODO: Get user input
        num1 = get_numbers(msg1)
        num2 = get_numbers(msg2)
        if not num1 or not num2:
            # if we didn't get a proper input, the loop will be broken by return
            print("Good bye!")
            return False
        # TODO: Compare numbers
        if num1 == num2:
            print("Both numbers are equal.")
        elif num1 > num2:
            print("The 1st number is greater.")
        else:
            print("The 2st number is greater.")


if __name__ == "__main__":
    # Here, if this file's been started directly, the main function will be started.
    main()
