# File: 11-Check_Files.py
# Author: Leandro Amaral Pereira
# Purpose: Practice Opening Files
# Reference: https://byui-cse.github.io/cse110-course/lesson11/checkpoint.html

with open("resources/books.txt") as books_list:
    for book in books_list:
        book = book.strip()
        print(book)