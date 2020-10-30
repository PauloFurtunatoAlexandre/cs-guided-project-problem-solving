"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.

# transform the argument in a list of integers in a new variable called numbers
# sort the numbers and reverse them to find the max and min
# test max and min in this list and return them using a join
# concatenate max and min into a string

"""


def max_and_min(input_str):
    numbers = list(map(int, input_str.split(" ")))
    numbers = sorted(numbers, reverse=True)
    max_and_min_numbers = [numbers[0], numbers[-1]]

    return " ".join([str(el) for el in max_and_min_numbers])


print(max_and_min("1 2 3 4 5"))  # -> "5 1"
print(max_and_min("1 2 -3 4 5"))  # -> "5 -3"
print(max_and_min("1 9 3 4 -5"))  # -> "9 -5"
