# File: 09-Check_Lists.py
# Author: Leandro Amaral Pereira
# Purpose: Practice working with lists.
# Reference: https://byui-cse.github.io/cse110-course/lesson09/checkpoint.html

friends_list = []
friend_name = ""

while friend_name != "End":
    friend_name = input("Type the name of a friend: ").capitalize()
    
    if friend_name != "End" and friend_name != "":
        friends_list.append(friend_name)

# To validate if the list has any entry
if friends_list:
    print("\nYour friends are:")

    for friend in friends_list:
        print(f"- {friend}")