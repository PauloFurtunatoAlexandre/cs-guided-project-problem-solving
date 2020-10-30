"""
Challenge #5:

Create a function that returns the data type of a given argument. There are
seven data types this challenge will be testing for:

- List
- Dictionary
- String
- Integer
- Float
- Boolean
- Date

Examples:
- data_type([1, 2, 3, 4]) ➞ "list"
- data_type({'key': "value"}) ➞ "dictionary"
- data_type("This is an example string.") ➞ "string"
- data_type(datetime.date(2018,1,1)) ➞ "date" 

Notes:
- Return the name of the data type as a lowercase string.
"""
import datetime


def data_type(value):
    # switcher = {
    #     'list': "List",
    #     'dict': "Dictionary",
    #     'str': "String",
    #     'int': "Integer",
    #     'float': "Float",
    #     'bool': "Boolean",
    #     'datetime.date': "Date"
    # }

    if type(value) == list:
        return "list"
    elif type(value) == dict:
        return "dictionary"
    elif type(value) == str:
        return "string"
    elif type(value) == int:
        return "integer"
    elif type(value) == float:
        return "float"
    elif type(value) == bool:
        return "boolean"
    else:
        return "date"


print(data_type([1, 2, 3, 4]))  # ➞ "list"
print(data_type({'key': "value"}))  # ➞ "dictionary"
print(data_type("This is an example string."))  # ➞ "string"
print(data_type(datetime.date(2018, 1, 1)))  # ➞ "date"
