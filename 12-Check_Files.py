# File: 12-Check_Files.py
# Author: Leandro Amaral Pereira
# Purpose: practice finding things in a list.
# Reference: https://byui-cse.github.io/cse110-course/lesson12/checkpoint.html

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

names_list = []
ages_list  = []

print()

for line in people:
    line = line.strip()
    name, age = line.split(" ")
    
    names_list.append(name)
    ages_list.append(int(age))

    print(f"Name: {name}, Age: {age}")

index_youngest = ages_list.index(min(ages_list))

print(f"\n{names_list[index_youngest]} is the youngest with {ages_list[index_youngest]} years")