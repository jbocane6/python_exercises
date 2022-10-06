"""
Define a function called swap_elements()that takes a list as argument
and replaces the first and last elements of that list.
"""

def swap_elements(l):
    l[0], l[-1] = l[-1], l[0]
    return l

print(swap_elements([4, 5, 6, 7]))
print(swap_elements([4, 5, 6, 7, 1]))
print(swap_elements([4, 5]))
