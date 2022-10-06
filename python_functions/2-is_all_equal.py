"""
Define a function called is_all_equal() that checks if the passed list consists of the same elements.
[IN]: is_all_equal([4, 5, 7])
[OUT]: False

[IN]: is_all_equal([4, 4, 4])
[OUT]: True
"""

def is_all_equal(nested_list):
    return len(set(nested_list)) <= 1

print(is_all_equal([4, 5, 7]))
print(is_all_equal([4, 4, 4]))
print(is_all_equal(['Q', 'Q', 'Q']))
print(is_all_equal(['Q', 'Q', 'DQ']))
