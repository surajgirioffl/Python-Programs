"""
    *Basic understanding of While loops*
"""

# program to print table of a number
number = int(input("\033[2J\033[HWrite a number to print it's table: "))

i = 1
while(i <= 10):
    print(number, "X", i, " = ", number*i)
    i += 1

"""
# infinite loop
while(True):  # we can also write while(anyIntegerExcept0)
    print("My name is your name.. (Press ctrl + C to terminate...)")
"""
