from collatz_class import Collatz
from time import time
from concurrent.futures import ProcessPoolExecutor, as_completed


# decorator to measure the execution time
def timer(f):
    def wrapper(*args, **kwargs):
        start = time()
        res = f(*args, **kwargs)
        exec_time = time() - start
        print(f"\nThe function {f.__name__} executed in: {exec_time:.3f} seconds")
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
def challenge(f, num):
    # TODO: get the biggest length and print the number and the length
    max_l = 0
    max_n = 0
    # use multiprocessing to finish the challenge faster
    w = 16  # processes number
    with ProcessPoolExecutor(max_workers=w) as ppe:
        # assume that odd numbers produce the longer chaines, but that's not certain.
        results = [
            ppe.submit(challenge_calc, n, num + 1, f, w * 2) for n in range(1, w * 2, 2)
        ]
        # check results of all processes and get the maximum value
        for p in as_completed(results):
            res = p.result()
            if res[1] > max_l:
                max_n, max_l = res
    # TODO: print the result
    print(f"The number {max_n} produces the longest chain of {max_l} steps.")


def challenge_calc(n, num, f, w):
    max_l = 0
    max_n = 0
    for i in range(n, num, w):
        lng = f(i)
        if lng > max_l:
            max_l = lng
            max_n = i
    return max_n, max_l


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
    # TODO: get input for challenge
    print("\nFind the number below the entered producing the longest Collatz chain.")
    # TODO: get input
    num = get_int_input()
    challenge(collatz.get_length, num)


if __name__ == "__main__":
    main()
