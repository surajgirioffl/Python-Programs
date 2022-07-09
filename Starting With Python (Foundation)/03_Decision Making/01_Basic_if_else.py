"""
    *Basic Understanding conditionals (if-else)*
    program to check that is user eligible to vote. 
    Assume: age below 18 is not not allowed to vote. 
"""

age = int(input("\033[2J\033[HWrite your age: "))
if age < 18:
    print("You are not eligible to vote..")
else:
    print("You are eligible to vote...")

# we can use one or more than one 'if' statement alone and check the conditions.
# But we can't user 'else' statement alone, it always follow with a 'if' statement.
# 'else' statement is optional.
