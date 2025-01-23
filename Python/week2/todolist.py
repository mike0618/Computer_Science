FILE = "todo.txt"

while True:
    print("--- Mike's Todo List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice: ").strip()

    match choice:
        case "1":
            inp = input("Enter the task: ").strip()
            if not inp:
                print("Wrong input.\n")
                continue
            with open(FILE, "a") as f:
                f.write(inp + "\n")
                print("Task added successully.\n")
        case "2":
            print("ToDo List: ")
            with open(FILE, "r") as f:
                for n, line in enumerate(f):
                    line = line.strip()
                    if line:
                        print(f"{n + 1}: {line.strip()}")
            print()
        case "3":
            num = input("Enter a line number: ").strip()
            if not num or not num[0].isdigit():
                print("Wrong input.\n")
                continue
            num = int(num)
            with open(FILE, "r") as f:
                lines = f.readlines()
            lng = len(lines)
            if num > lng:
                print("This line does not exist.\n")
                continue
            lines.pop(num - 1)
            with open(FILE, "w") as f:
                f.writelines(lines)
            print(f"The line {num} removed successully.\n")
        case _:
            break
