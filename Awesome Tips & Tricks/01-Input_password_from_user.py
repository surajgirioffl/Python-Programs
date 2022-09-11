"""
    * Program to input password without displaying the password on console.
    * To fetch current logged-in username or login name from system.
"""
from getpass import getpass, getuser

username = input("write username (press enter for system username): ")
if username == "":
    username = getuser()  # fetch username from system
password = getpass("write password: ")  # hide password on console

print(f"Username: {username} and Password: {password}")
