"""
Define a function called is_nested() that checks if the passed list is nested and consists of elements of type list (a list of lists).
[IN]: is_nested([[3, 4], [2, 1]])
[OUT]: True

[IN]: is_nested([[3, 4], 0, [2, 1]])
[OUT]: False
"""

def is_nested(array):
    if len(array) == 0:
        return False
    return all(isinstance(row, list) for row in array)

print(is_nested([[3, 4]]))
print(is_nested([[3, 4], 4]))
print(is_nested([[3, 4], [2, 1]]))
print(is_nested([[3, 4], 0, [2, 1]]))
