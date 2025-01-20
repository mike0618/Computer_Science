"""
Fibonacci sequence

Manual calculation:
0 1 --> 0+1=1
0 1 1 --> 1+1=2
0 1 1 2 --> 1+2=3
0 1 1 2 3 --> 2+3=5
0 1 1 2 3 5 --> 3+5=8
0 1 1 2 3 5 8 --> 5+8=13
0 1 1 2 3 5 8 13 --> ...

"""


def fib_calc(n: int) -> list:
    seq = []
    if n > 0:  # return empty for 0 and negative numbers
        a, b = 0, 1
        for _ in range(n):
            seq.append(str(a))  # create a list with strings to use join later
            a, b = b, a + b  # Fibonacci calculation
    return seq


def main():
    # create a title
    title = "|   Fred's Fibonacci Sequence Formulator   |"
    line = "+" + "-" * (len(title) - 2) + "+"
    print(line)
    print(title)
    print(line)
    # let the user to try it many times with a loop
    while True:
        num = input("Enter the number of Fibonacci numbers to be printed: ").strip()
        if not num:  # break it if no input
            print("Bye!")
            break
        if not num.isdigit():  # some input handling
            print("Input is wrong, try again")
            continue
        print(" ".join(fib_calc(int(num))))  # show result


if __name__ == "__main__":
    main()
