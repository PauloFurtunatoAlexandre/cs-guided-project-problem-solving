"""
Challenge #8:

Given an integer, write a function that returns "Even" for even integers and
"Odd" for odd integers.

Examples:
- parity(0) -> "Even"
- parity(1) -> "Odd"
- parity(2) -> "Even"

# check if argument is odd and return "Odd"
# check if argument is even and return "Even"

"""
def parity(input_int):
    if input_int % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(parity(0)) # -> "Even"
print(parity(1)) # -> "Odd"
print(parity(2)) # -> "Even"
