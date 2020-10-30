"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.

# iterate the argument and check each charact to confirm if it is a string
# We will consider `a, e, i, o, u as vowels for this challenge (but not y)

"""
def get_count(input_str):
    counter = 0
    for i in input_str:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            counter = counter + 1
    return counter


print(get_count("agora vai"))
print(get_count("time to go"))
print(get_count("this is Python"))
print(get_count("you cannot stop me"))