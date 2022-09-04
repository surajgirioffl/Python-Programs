"""
    01) String formatting using old C-like format specifiers.
"""
# printing string
name = "My name is your name"
print("Name: %s" % name)

# printing integer
number = 120
print("Number: %d" % number)

# printing float
value = 120.998
print("Value: %f" % value)

# printing multiple data
print("Printing All..")
print("Name = %s & Number=%d & Value=%f" % (name, number, value))
