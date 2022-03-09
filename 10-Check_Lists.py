# File: 10-Check_Lists.py
# Author: Leandro Amaral Pereira
# Purpose: Practice working with list indexes.
# Reference: https://byui-cse.github.io/cse110-course/lesson10/checkpoint.html

items_list = []
item_name = ""

def show_list():
    print("\nThe shopping list is:")

    for item in items_list:
        print(f"{item}")

def show_indexed_list():
    print("\nThe shopping list with indexes is:")

    for i in range(len(items_list)):
        print(f"{i}. {items_list[i]}")

while item_name != "Quit":
    item_name = input("Please enter the items of the shopping list (type: quit to finish): ").capitalize()
    
    if item_name != "Quit" and item_name != "":
        items_list.append(item_name)

# To validate if the list has any entry
if items_list:
    
    show_list()
    show_indexed_list()

    index = int(input("\nWhich item would you like to change? "))
    new_item = input("What is the new item? ").capitalize()
    items_list[index] = new_item

    show_indexed_list()