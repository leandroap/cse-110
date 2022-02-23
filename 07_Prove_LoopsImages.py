# Week 07 Prove: Assignment - Loops and images
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse110-course/lesson07/prove.html

# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open("images/beach.jpg")

# This line attempts to open a new window to display the image.
image_original.show()

pixels_original = image_original.load()
print(f"Size: {image_original.size}")

x = 100
y = 201

while x < 200:
    r, g, b = pixels_original[x, y]
    print(f"r: {r} g: {g} b: {b}")
    pixels_original[x, y] = (255, 0, 0)
    x = x + 1

x = 100
y = 201

while y > 50:
    r, g, b = pixels_original[x, y]
    print(f"r: {r} g: {g} b: {b}")
    pixels_original[x, y] = (255, 0, 0)
    y = y - 1

image_original.show()