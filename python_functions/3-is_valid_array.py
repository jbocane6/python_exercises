"""
Two functions are given below:

is_nested(array) 
is_all_equal(nested_List)

Define a function called is_valid_array()
that checks if a matrix can be built from the passed list.
You can use the given functions in your solution.
The passed list must be a nested list, and each nested list
should consist of the same number of elements.
"""

def is_nested(array):
    if len(array) == 0:
        return False
    return all(isinstance(row, list) for row in array)


def is_all_equal(nestedList):
    return len(set(nestedList)) <= 1

def is_valid_array(array):
    return is_nested(array) and is_all_equal([len(x) for x in array])

print(is_valid_array([[3], [4]]))
print(is_valid_array([[3, 4], [4, 5]]))
print(is_valid_array([[3, 4, 5], [4, 5]]))
print(is_valid_array([[3, 4], [4, 5], [3, 1]]))
print(is_valid_array([[]]))
