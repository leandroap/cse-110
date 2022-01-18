# File: 03-Check_Numbers.py
# Author: Leandro Amaral 
# Purpose: Practice using mathematical expressions
# Reference: https://byui-cse.github.io/cse110-course/lesson03/checkpoint.html

user_age = int(input("How old are you? "))
user_age += 1

print(f"On your next birthday, you will be {user_age}\n")

eggs_cartons = int(input("How many egg cartons do you have? "))
eggs = eggs_cartons * 12

print(f"You have {eggs} eggs\n")

cookies = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))

print(f"Each person may have {cookies / people} cookies\n")