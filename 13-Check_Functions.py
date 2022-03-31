# File: 13-Check_Functions.py
# Author: Leandro Amaral Pereira
# Purpose: practice writing basic functions
# Reference: https://byui-cse.github.io/cse110-course/lesson13/checkpoint.html

def display_regular(message):
    print(message)

def display_uppercase(message):
    print(message.upper())

def display_lowercase(message):
    print(message.lower())

the_message = input("\nWhat is your message? ")

display_regular(the_message)
display_uppercase(the_message)
display_lowercase(the_message)