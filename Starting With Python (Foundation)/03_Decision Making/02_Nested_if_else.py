"""
    *Basic understanding of Nested if-else*
    program to find greatest number in given 3 number.
"""

a, b, c = input("write 3 number (space separated): ").split()
a = int(a)
b = int(b)
c = int(c)

if a > b:
    if(a > c):
        # print() will auto add space between number & string
        print(a, "is greatest number...")
    else:
        print(c, "is greatest number...")
else:
    if(b > c):
        print(b, "is greatest number...")
    else:
        print(c, "is greatest number...")
