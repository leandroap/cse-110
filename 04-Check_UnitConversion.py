# File: 04-Check_UnitConversion.py
# Author: Leandro Amaral 
# Purpose: Converting between different types of units
# Reference: https://byui-cse.github.io/cse110-course/lesson04/checkpoint.html


fahrenheit_temperature = float(input("What is the temperature in Fahrenheit? "))

celsius_temperature = (fahrenheit_temperature - 32) * (5 / 9)

print(f"The temperature in Celsius is {celsius_temperature:.1f} degrees.\n")
