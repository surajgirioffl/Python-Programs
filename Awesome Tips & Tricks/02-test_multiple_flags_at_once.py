# Trick to test multiple flags at once

a, b, c = 2, 1, 0

# ---------------------OR------------------
# Normal way to test values
if a == 2 or b == 2 and c == 2:
    print("Any of a,b,c is 2")

# test at once
if 2 in (a, b, c):
    print("a,b and c are same.")


# Normal way to test boolean values
if a or b or c:
    print("Any of a or b or c is True.")

# test at once
if any((a, b, c)):
    print("Any of a or b or c is True.")

# About any() built-in global function
"""
Syntax: any()
any(iterable)-> bool
any() function returns True if any element of the iterable is True else False.
* True means Non-Zero value.
* False means Zero value.
* if iterable is empty, it returns False.
Iterables are string, list, tuple, dictionary and set.
"""
