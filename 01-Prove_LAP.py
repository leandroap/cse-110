# 01-Prove_LAP.py
# Author: Leandro Amaral Pereira

userName = input("Hi, my name is Leandro. What is your name? Type here please: ")

if userName:
    print("Nice to meet you " + userName + ".")
else:
    print("Ok, let's try a different question.")

userColor = input("Please type your favorite color: ")

if userColor:
    print("Your favorite color is " + userColor + ".")

    if userColor.upper() == "BLUE":
        print("I like the color Blue also")
    else:
        print("My favorite color is Blue")

else:
    print("Ok, you can tell me it later, bye.")