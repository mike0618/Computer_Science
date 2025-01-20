# Import our function from our module
from factorial import factorial

title = "| Frank's Factorial Factory |"
line = "-" * len(title)


def print_title():
    """
    Print a creative program title
    """
    print(line)
    print(title)
    print(line)


def get_input():
    """
    Get user input
    """
    inp = input("Enter a whole number: ").strip().replace(",", "")
    if inp.isdigit():
        return int(inp)
    return False


def menu():
    """
    Menu loop
    """
    while True:
        number = get_input()
        if not number:
            print("Good bye.")
            break
        print(f"The factorial of {number} is {factorial(number):,.0f}\n{line}")


def main():
    """
    Main function
    """
    print_title()
    menu()


if __name__ == "__main__":
    main()
