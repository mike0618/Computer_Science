from collatz_class import Collatz
from time import time


# decorator to measure the execution time
def timer(f):
    def wrapper(*args, **kwargs):
        start = time()
        res = f(*args, **kwargs)
        exec_time = time() - start
        print(f"\n The function {f.__name__} executed in: {exec_time:.3f} seconds")
        return res

    return wrapper


def get_int_input():
    # get the correct input
    while True:
        num = input("Enter a whole number: ").strip().replace(",", "")
        if num.isdigit():
            num = int(num)
            return num
        print("Wrong input.")


@timer
def challenge(f):
    # TODO: get input for challenge
    print("\nFind the number below the entered producing the longest Collatz chain.")
    # TODO: get input
    num = get_int_input()
    # TODO: get the biggest length and print the number and the length
    max_l = 0
    max_n = 0
    # assume that odd numbers produce the longer chaines, but that's not certain.
    for n in range(1, num, 2):
        lng = f(n)
        if lng > max_l:
            max_l = lng
            max_n = n
    # TODO: print the result
    print(f"The number {max_n} produces the longest chain of {max_l} steps.")


def main():
    collatz = Collatz()
    print("The Collatz chain for the entered number.")
    # TODO: get input
    num = get_int_input()
    # TODO: get chain and print it with its length
    chain = collatz.get_lst(num)
    print(" ".join(chain))
    print(f"Steps: {len(chain)}")

    # TODO: Challenge
    challenge(collatz.get_length)


if __name__ == "__main__":
    main()
