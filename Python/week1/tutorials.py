"""
Work with Files
Author: Mikhail Zubko
"""

import json

print("Tutorial 10.1: Reading a Text File\n")
#
# Create a File and add some content
with open("example.txt", "w") as f:
    f.write("Hello\nThis is a sample text file.\nBye!")

# Open a file
file = open("example.txt", "r")
# Read the entire content
content = file.read()
# Close the file
file.close()
# Print the content str
print(content)
# Using "with"
# Creates a file object and closes the file automatically
# modes: r - read, w - write, a - append, x - exclusive creation, fails if the file already exists
with open("example.txt", "r") as file:
    content = file.read()
# the file desc is automatically closed after the deindent
print(content)

print("\nTutorial 10.2: Writing a Text File\n")
# Catch any exceptions
try:
    # Create a new file and write into it
    with open("rockstart.txt", "w") as rockfile:
        rockfile.write("Eddie Van Halen\n")
        rockfile.write("Eric Clapton\n")
        rockfile.write("Steve Gadd\n")

    print("File written successfully.")
except Exception as e:
    print(f"The file was not written: {e}")

print("\nTutorial 10.3: Reading the file line by line\n")
try:
    with open("rockstart.txt") as rockfile:
        # print(rockfile.read())
        # there is a loop instead of the readline() function.
        for line in rockfile:
            print(line.rstrip())  # strip a new line character
        print("The file was successfully read.")
except Exception as e:
    print(f"Something went wrong: {e}")

print("\nTutorial 10.4: Appending to a text file\n")

# Append to the file
with open("rockstart.txt", "a+") as rockfile:
    rockfile.write("Eddie Van Halen\n")
    rockfile.write("Eric Clapton\n")
    rockfile.write("Steve Gadd\n")
    rockfile.seek(0)  # go to the beginning of the file
    print(rockfile.read())

print("\nTutorial 10.5: Writing numbers to a file\n")
NUM_FILE = "numbers.txt"

with open(NUM_FILE, "w") as f:
    # Get three numbers as int from the user
    n1 = int(input("Enter a whole number: "))
    n2 = int(input("Enter another whole number: "))
    n3 = int(input("Enter another whole number: "))
    # write numbers into the file using f-strings
    f.write(f"{n1}\n")
    f.write(f"{n2}\n")
    f.write(f"{n3}\n")
    print(f"File {NUM_FILE} written successfully.")

print("\nTutorial 10.6: Read numbers from the file\n")

with open(NUM_FILE) as f:
    n1 = int(f.readline())
    n2 = int(f.readline())
    n3 = int(f.readline())
    total = n1 + n2 + n3
    print(f"The numbers are: {n1} {n2} {n3}")
    print(f"The total is: {total}")

print("\nTutorial 10.7: Reading and Writing to a text file\n")

C_TEMP = "ctemps.txt"
F_TEMP = "ftemps.txt"

with open(C_TEMP, "w+") as cf, open(F_TEMP, "w") as ff:
    # write the initial data
    for t in ("32.0\n", "0.0\n", "24.0\n", "-40\n"):
        cf.write(t)
    cf.seek(0)
    # convert and write the temperatures
    for ctemp in cf:
        ftemp = float(ctemp) * 1.8 + 32
        ff.write(f"{ftemp}\n")
        # show the progress
        print(f"{ctemp.rstrip()}°C = {ftemp}°F")

print("\nTutorial 10.8: Dumping and Loading a JSON File\n")

FILE = "numbers.json"
numbers = [2, 3, 4, 6, 7, 89]
with open(FILE, "w") as f:
    # serialize the list into JSON and write into the file
    json.dump(numbers, f)

with open(FILE) as f:
    # load the JSON and store into a nums variable, then print it.
    nums = json.load(f)
    print(nums)


print("\nAssignment 1: Serialize Yourself Baby\n")

FILE = "personal_info.json"

try:
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: ").strip())
    hobbies = input("Enter your hobbies (comma separated): ").strip().split(",")

    data = {"name": name, "age": age, "hobbies": hobbies}
    # serialize the date into JSON
    with open(FILE, "w") as f:
        json.dump(data, f)
        print(f"Serialized successfully to {FILE}")
    # load the data from the file
    with open(FILE) as f:
        print("Loaded data:")
        print(json.load(f))

except Exception as e:
    print(f"Something went wrong: {e}")
