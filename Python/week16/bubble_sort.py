from random import randint

lst = [randint(0, 99) for _ in range(99)]
R = range(len(lst) - 1)
print("Python Bubble Sort\n")
print(lst)
swap = True
while swap:
    swap = False
    for i in R:
        if lst[i] > lst[i + 1]:
            swap = True
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
print()
print(lst)
