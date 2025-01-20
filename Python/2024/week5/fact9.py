# define some variables
n = 9
fact = 1
# add some list-comprehention and walrus magic here ;)
[
    print(f"After multiplying by {i}, factorial is now {(fact := fact * i):,.0f}")
    for i in range(1, n + 1)
]
# print the result
print("-" * 80, f"\nThe factorial of {n} is {fact:,.0f}")
