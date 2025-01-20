from utils import get_title, get_float
import convert

functions = (
    ("(1) Centimeters --> Inches", convert.cm_to_inches),
    ("(2) Inches --> Centimeters", convert.inches_to_cm),
    ("(3) Kilometers --> Miles", convert.km_to_miles),
    ("(4) Miles --> Kilometers", convert.miles_to_km),
)


def main():
    # TODO: print a heading
    print(get_title("Mickey's Multiple Unit Converter"))
    while True:
        # TODO: display menu
        print("Choose a conversion:")
        for f in functions:
            print(f[0])
        # TODO: get user's choice
        choice = input("Enter your choice: ").strip()
        # TODO: define a target function and the origin unit
        func = None
        origin = None
        match choice:
            case "1":
                origin = "Centimeters"
                func = functions[0][1]
            case "2":
                origin = "Inches"
                func = functions[1][1]
            case "3":
                origin = "Kilometers"
                func = functions[2][1]
            case "4":
                origin = "Miles"
                func = functions[3][1]
            case _:
                print("Wrong input. Try again")
                continue
        # TODO: get user input as a float
        fl_input = get_float(f"Enter {origin}: ")
        if fl_input is None:
            print("You entered nothing.")
        else:
            # TODO: print result
            print(func(fl_input))
        # TODO: ask about another conversion
        ans = input("Another conversion? (y/N): ").lower().strip()
        if ans != "y":
            break


if __name__ == "__main__":
    main()
