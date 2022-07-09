"""
    *Basic understanding of if-else-if ladder*
    program to display result of a subject after input of marks.
     
"""
marks = int(input("Write your marks (within 100): "))
if marks < 30:
    print("Result: Fail...")
elif marks >= 30 and marks < 50:
    print("Result: 3rd Class...")
elif marks >= 50 and marks < 80:
    print("Result: 2nd Class...")
else:
    print("Result: 1st Class...")
