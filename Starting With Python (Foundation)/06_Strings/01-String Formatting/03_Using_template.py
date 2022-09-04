"""
    03) String formatting using 'Template' class of 'string' module.
"""
from string import Template

name = "Suraj Giri"
roll = 10
interest = "Python"

myStr = Template("Name: $name && Roll: $myRoll && Interest=$interest")
print(myStr.substitute(name=name, myRoll=roll, interest=interest))

# inside string double quotes the variable name after '$' has no relation with any variable name.
# we can write same var name inside string double quotes or others no issue because it will remain new and undefined until we pass it as a keyword argument to the 'substitute' method explicitly.
