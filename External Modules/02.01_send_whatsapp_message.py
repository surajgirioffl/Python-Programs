import time
from pywhatkit import whats as kit
from time import sleep
import pyautogui as gui
# for i in range(10):
kit.sendwhatmsg_instantly(
    "+91 8227974640", "Hii this is suraj", 5, False, 300)
gui.click()  # it will click where mouse is pointing
gui.press("enter")
