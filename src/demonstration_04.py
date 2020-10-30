"""
Challenge #4:

Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :)
grin -> :D
sad -> :(
mad	-> :P

Examples:
- emotify("Make me smile") ➞ "Make me :)"
- emotify("Make me grin") ➞ "Make me :D"
- emotify("Make me sad") ➞ "Make me :("

Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.


-we might want to use a dictionary to store the key value pairs
{
    "smile": ":)"
    "grin": ":D"
    "sad": ":("
    "mad": ":P"
}

# iterate over the hash tables items extrapolating the key and value of each item
# use a string ".replace" to replace the substring of the key with the value

"""


def emotify(txt):
    # Your code here O(n)
    # first pass
    # data = {
    #     "smile": ":)",
    #     "grin": ":D",
    #     "sad": ":(",
    #     "mad": ":P"
    # }

    # for k, v in data.items():
    #     txt = txt.replace(k, v)

    # return txt

    # second pass O(1)
    data = {
        "smile": ":)",
        "grin": ":D",
        "sad": ":(",
        "mad": ":P"
    }

    start_of_string = txt[:8]
    
    end_of_string = txt[8:]
    
    full_string = start_of_string + data[end_of_string]
    
    return full_string


print(emotify("Make me smile"))  # "Make me :)"
print(emotify("Make me grin"))  # "Make me :D"
print(emotify("Make me sad"))  # "Make me :("
print(emotify("Make me mad"))  # "Make me :P"
