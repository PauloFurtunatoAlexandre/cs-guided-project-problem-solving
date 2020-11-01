"""
Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"

# create a new list where you can enumerate the characters by bringing each character multiplied by value of its current index
# capitalize the first letter on each segment
# join all segments in a string again using the "-" character


"""


def repeat_it(input_str):
    letters_list = []
    for k, v in enumerate(input_str):
        letters_list.append((((k+1) * v)).capitalize())

    input_str = "-".join(letters_list)

    return input_str


print(repeat_it("abcd"))  # -> "A-Bb-Ccc-Dddd"
print(repeat_it("RqaEzty"))  # -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(repeat_it("cwAt"))  # -> "C-Ww-Aaa-Tttt"
