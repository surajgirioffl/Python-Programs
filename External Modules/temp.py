import time
from pywhatkit import whats as kit
from time import sleep
import pyautogui as gui
# for i in range(10):
kit.sendwhatmsg_instantly(
    "+91 8227974640", "Hii this is suraj\t\n", 5, False, 300)
gui.click(1050, 950)
time.sleep(2)
# gui.press_and_release('enter')

# flask need to be install
#pywhatkit is installed
#playsound is installed
