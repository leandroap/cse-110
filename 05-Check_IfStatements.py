# File: 05-Check_IfStatements.py
# Author: Leandro Amaral 
# Purpose: Practicing If Statements
# Reference: https://byui-cse.github.io/cse110-course/lesson05/checkpoint.html

## COMPARING NUMBERS
firt_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))

if firt_number > second_number:
    print("The first number is greater")
else:
    print("The first number is not greater")

if firt_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if firt_number < second_number:
    print("The second number is greater")
else:
    print("The second number is not greater")

## COMPARING STRINGS
user_favorite_animal = input("\nWhat is your favorite animal? ").lower()

if "bear" == user_favorite_animal:
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")




