# basic output in python
age = 18
# in print() we use comma operator (',') to print more than one content in python
# printing using print() is like printing using cout object in c++. But print() uses ',' operator instead of '<<' (insertion) to print more than one item.
# cout is an object in c++ but here print() is a function.
# in java we use '+' operator in println()/print() member function to print more than one item. And in python, we use ',' operator instead of '+'
# Actually, it's from C language printf(). But in python, we don't need to use format specifiers.
print("Your age is ", age, " and you are eligible to vote\n")


# we can use 1. '..' OR 2. ".." OR 3. '''..''' OR 4. """..""" to specify the string
# If our string contains any of ",',''' etc then we use other specification method from above 4 except one/more which is used in our string
# simply, the control search for that character for string termination from which the string was started (leading character)
print("My name is your name")
print('My name is your name')
print('''My name is your name''')
string = "suraj kumar giri"
number = 14
print("%s" % string)
print("%d" % number)
# To print more than one line
