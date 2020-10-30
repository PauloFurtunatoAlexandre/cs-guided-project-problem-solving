"""
Challenge #3:

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- Bonus: Try to complete this challenge in one line!
# transfor the string into numbers separated by commas
    # need a variable to hold the new value, possible usage of map to create a new list of numbers with split those numbers
# calculate the product of those numbers
    
"""


def multiply_nums(nums):
    new_values = []
    product = 1

    new_values = list(map(int, nums.split(", ")))

    for i in new_values:
        product = product * i

    return product


print(multiply_nums("2, 3"))  # ➞ 6
print(multiply_nums("1, 2, 3, 4"))  # ➞ 24
print(multiply_nums("54, 75, 453, 0"))  # ➞ 0
print(multiply_nums("10, -2"))  # ➞ -20
