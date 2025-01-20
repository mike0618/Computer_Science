# tutorial 1: Loops

# define a list
nums = [1, 3, 5]

# iterate through it
for n in nums:
    print(n)

# iterate through indices
for i in range(len(nums)):
    # multiply each num by 2
    nums[i] *= 2
    # print num along with their indices
    print(f"{i+1}. {nums[i]}")

print()

# tutorial 2: Slicing

# sliting a range from a list
nums = list(range(1, 6))
subset = nums[1:4]
print(subset)
# a string
text = "PythonProgramming"
substr = text[:6]
print(substr)

print()

# with step
even = nums[::2]
print(even)
# from a string
every_2nd_ch = text[::2]
print(every_2nd_ch)
# from the end
last3 = nums[-3:]
print(last3)
# modifying elements
fruits = ["apple", "banana", "cherry", "date"]
fruits[1:3] = ["pear", "grape"]
print(fruits)

print()

# tutorial 3: List functions
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums) / len(nums))
print(sorted(nums))
# "in" operator
if 3 in nums:
    print("Your list contains 3")
# not "in"
if 0 not in nums:
    print("Your list has no zeroes")

print()

# List methods
mylist = ["a", "b", "c"]
print("Original:", mylist)
mylist.append("d")
print(f"Append: {mylist}")
mylist.insert(1, "d")
print(f"Insert: {mylist}")
mylist.sort()
print(f"Sort: {mylist}")
mylist.reverse()
print(f"Reverse: {mylist}")
print(f"Index b: {mylist.index('b')}")
print(f"Count b: {mylist.count('b')}")
mylist.remove("b")
print(f"Remove b: {mylist}")
popped = mylist.pop(1)
print(f"Pop {popped}: {mylist}")
mylist.extend(mylist)
print(f"Extend: {mylist}")
sep = " | "
mylist = sep.join(mylist)
print(f"Separator: {mylist}")

print()

# tutorial 4: try except
print("Fahrenheit Converter")
try:
    # if user doesn't enter a number an exceptio is raised
    fah = float(input("enter fahrenheit t: "))
    # if no exception
    cel = 5 * (fah - 32) / 9
    print(cel)
except ValueError as v:
    # specific ValueError exception
    print(f"Please enter a number\n{v}")
except Exception as e:
    # handle any other exceptions
    print(f"Something went wrong\n{e}")
