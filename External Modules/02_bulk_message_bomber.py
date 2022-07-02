from pyautogui import write, press
from time import sleep


def addSubStringAfterIndex(originalString, index, substring):
    '''This function will add passed substring after given index of the string'''
    newString = originalString[:index]+substring+originalString[index+1:]
    return newString


i = 1
originalString = "What is your name? "
while i <= 1000:
    if i == 1:
        sleep(5)
    string = addSubStringAfterIndex(
        originalString, len(originalString), str(i))
    write(string)
    press("enter")
    i += 1
