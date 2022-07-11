"""
    Basic understanding of control statements of loop in python
    Understanding of 'break' & 'continue' statements
"""

i = 0
while(True):
    if i == 5:
        print("Encounter with continue statement at i=5....")
        i += 1  # it is compulsory else i remains 5 and loop will become infinite
        # if this suite will execute then control will continue to next iteration. And all below codes of current iteration will not be executed.
        continue
    if i == 10:
        print("Encounter with break statement at i=10....")
        # whenever control encounters with 'break' statement then it simply come out from suite of loop.
        break
    print(i)
    i += 1
