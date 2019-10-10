# 1 - Lists

# given list

numbers = [1, 2, 3, 4]

# Task 1 - Create a new list, calculating the square number (x * x) for each item in the numbers lit
# Expected output:
# [1, 4, 9, 16]

# Solution 1
square = lambda x: x**2
powered = []
for number in numbers:
    powered.append(square(number))

print(powered)


# Task 2 - Filter all the even numbers in the list
# Expected output: [2, 4]


# Task 3 - Sum all the odd numbers in the list
# Expected output: 4