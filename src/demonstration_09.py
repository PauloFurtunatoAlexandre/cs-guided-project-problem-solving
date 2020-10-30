"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""


def get_middle(input_str):
    # Your code here
    # check the string to confirm if it is odd or even
    # if even need to return 2 middle characters in the middle
    # if odd just return 1 character in the middle
    # find out the length of the string and bring the middle index using a variable
    # make sure the number is usable as index and floor it
    # python can use a divider // for floor
    # need to use slice to return only the value in the middle [middle_index - 1: middle_index + 1] for even length and [middle_index: middle_index - 1] for odd length
    str_len = len(input_str)
    middle_index = str_len // 2
    if str_len % 2 == 0:
        return input_str[middle_index - 1: middle_index + 1]
    else:
        return input_str[middle_index: middle_index + 1]


print(get_middle("test"))  # -> "es"
print(get_middle("testing"))  # -> "t"
print(get_middle("middle"))  # -> "dd"
print(get_middle("A"))  # -> "A"
