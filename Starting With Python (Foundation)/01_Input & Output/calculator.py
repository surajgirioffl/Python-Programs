num1 = int(input("Write number 1: "))
num2 = int(input("Write number 2: "))

while(True):
    print("\nWrite 1 for sum")
    print("write 2 for subtract")
    print("write 3 for multiply")
    print("write 4 for divide")
    print("write 5 for remainder")
    print("write 6 for power")
    print("Press 0 to exit")
    choice = input("write your choice:")
    if choice == "":  # means user has pressed enter without writing anything.
        print("\033[2J\033[H")
        continue
    choice = int(choice)

    if choice == 1:
        print("The sum of ", num1, " and ", num2, " is ", num1+num2)
    elif choice == 2:
        print("The subtract of ", num1, " and ", num2, " is ", num1-num2)
    elif choice == 3:
        print("The multiply of ", num1, " and ", num2, " is ", num1*num2)
    elif choice == 4:
        print("The divide of ", num1, " and ", num2, " is ", num1/num2)
    elif choice == 5:
        print("The remainder of ", num1,
              " divided by ", num2, " is ", num1 % num2)
    elif choice == 6:
        print("The power of ", num1, " to ", num2, " is ", num1**num2)
    elif choice == 0:
        break
    else:
        print("Invalid choice.")
