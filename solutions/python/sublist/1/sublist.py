"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if _is_contiguous_subseq(needle=list_one, haystack=list_two):
        return SUBLIST
    if _is_contiguous_subseq(needle=list_two, haystack=list_one):
        return SUPERLIST
    return UNEQUAL

        
def _is_contiguous_subseq(*,needle, haystack):
    if len(needle) == 0:
        return True
    if len(needle) > len(haystack):
        return False
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:  
            return True
    return False
