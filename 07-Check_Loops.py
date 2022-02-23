# File: 07-Check_Loops.py
# Author: Leandro Amaral Pereira
# Purpose: Practice while loops.
# Reference: https://byui-cse.github.io/cse110-course/lesson07/checkpoint.html

number = int(input("Please type a positive number: ") or -1)

while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: ") or -1)

print(f"The number is: {number}\n\n")

answer = ""

while answer != "yes":
    answer = input("May I have a piece of candy? ").lower()

print("Thank you.")


