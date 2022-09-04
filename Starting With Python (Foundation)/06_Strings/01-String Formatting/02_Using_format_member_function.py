"""
    02) String formatting using 'format' member function of <class str>
"""

# ----------------------------------------------------------------
# 1) Using blank curly braces
# printing single data
name = "Giri"
print("Name: {}".format(name))

# printing multiple data
marks = 99
roll = 10
sem = "3rd"
# data will be printed in the order of parameters passed to format method.
print("Name: {} && Marks: {} && Roll: {} && Sem: {}".format(name, marks, roll, sem))


# ----------------------------------------------------------------
# 2) Using positional(by index) curly braces (starts from 0)
print("Name: {0} && Marks: {1} && Roll: {2} && Sem: {3}".format(name, marks, roll, sem))
# index is based on the order of arguments passed to the format function. First argument is at index 0, second at index 1 and so on.
# If you want to use the same argument multiple times, you can pass the index of that argument multiple times.
print("{3} {2} {1} {0}".format(name, marks, roll, sem))
# output will: 3rd 10 99 Giri

# ----------------------------------------------------------------
# 3) Using variable names in curly braces
# variable name written inside curly braces is the name of the variable that will be replaced with the value of that variable in format method
# variable name written inside curly braces are not pre-defined. So, we have to pass the variable name explicitly as a keyword argument to the format method
print(
    "Name: {myName} && Marks: {marks} && Roll: {classRoll} && Sem: {sem}".format(
        myName=name, marks=marks, classRoll=roll, sem=sem
    )
)
# So, inside curly braces, we can use any variable name. And while calling the format method, we have specify the variable name and it's value explicitly as a keyword argument.
# keep in mind, the variable name inside the curly braces has no relation b/w already defined variable. We can use them but then also we have to pass the variable name explicitly as a keyword argument to the format method (and it's get defined that time).
# variable name is written for better readability and understanding of the code.
