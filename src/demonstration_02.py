"""
Challenge #2:

Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.

# add the number on the index with the value of the current index, need to find out the built in method which can return the index number = "len"
# loop through the list and add the index value to the current number
# create a new_numbers and return the new values
"""

def add_indexes(numbers):
    # Your code here
    # index_values = []
    new_numbers = []
    # for i in range(len(numbers)):
    #     index_values.append(i)
    # for i in range(0, len(numbers)):
    #     new_numbers.append(numbers[i] + index_values[i])
    
    for el in enumerate(numbers):
        new_numbers.append(el[0] + el[1])
    return new_numbers
    

print(add_indexes([0, 0, 0, 0, 0])) # ➞ [0, 1, 2, 3, 4]
print(add_indexes([1, 2, 3, 4, 5])) # ➞ [1, 3, 5, 7, 9]
print(add_indexes([5, 4, 3, 2, 1])) # ➞ [5, 5, 5, 5, 5]