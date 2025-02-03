from threading import Thread
from time import sleep, time
from concurrent.futures import ThreadPoolExecutor


def f1():
    for i in range(5):
        print("ONE", i)
        sleep(0.5)


def f2():
    for i in range(5):
        print("TWO", i)
        sleep(0.5)


def f3():
    for i in range(5):
        print("THREE", i)
        sleep(0.5)


funcs = (f1, f2, f3)


def main():
    print("Without Threading")
    start = time()
    [f() for f in funcs]
    print("Time usage: ", time() - start)

    print("With Threading")
    start = time()
    threads = [Thread(target=f) for f in funcs]
    [t.start() for t in threads]
    # pause the main program until the thread is complete
    [t.join() for t in threads]
    print("Time usage: ", time() - start)

    print("Using ThreadPoolExecutor")
    start = time()
    with ThreadPoolExecutor(max_workers=3) as tpe:
        threads = [tpe.submit(f) for f in funcs]
        [t.result() for t in threads]
    print("Time usage: ", time() - start)


if __name__ == "__main__":
    main()
