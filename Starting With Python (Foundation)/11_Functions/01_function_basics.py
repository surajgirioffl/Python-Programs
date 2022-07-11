"""
    *Basic understanding of function"
"""

# take arguments of two string and add string 1 in end of string 2 with space and return the new string
# it is a global function


def stringConcat(string1, string2):
    return string1 + " " + string2


firstName = input("Write your first name: ")
lastName = input("Write your last name: ")
print("Your name is ", stringConcat(firstName, lastName))
