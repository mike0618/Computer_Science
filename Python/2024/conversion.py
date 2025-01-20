import converter  # import created before module with functions

line = "-" * 80
while True:
    print(line)
    print("\nConvert Gallons to Liters (default)\n")
    # set default conv function G to L
    conv = converter.gallons_to_liters
    # ask user for a conversion way
    way = input("To convert Liters to Gallons input L: ").upper()
    if way == "L":
        print("Convert Liters to Gallons")
        # change conv function if user input L
        conv = converter.liters_to_gallons
    # ask user to input a value or nothing to exit
    user_input = input("\nEnter the value (empty input to exit): ")
    # exit if user input nothing.
    if not user_input:
        break
    # try except block, to catch value error
    try:
        # trying to convert user input to float and run convert function
        print(line)
        conv(float(user_input))
    except ValueError:
        print("Input is incorrect, try again.")
