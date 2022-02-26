# Week 08 Prove: Assignment - Loops and images
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse110-course/lesson07/prove.html

import datetime
line = "\n**********************************************\n"
print(f"{line}*      Welcome to the Looping Activity       *{line}")

# This line imports or includes the library we will need
from PIL import Image

# Set here the folder where the images are
images_path = "images/"

# List of images we will use as a possible background
backgrounds = ["beach.jpg", "snowscape.jpg", "desert.jpg", "field.jpg", "forest.jpg"]

print("In this activity we will take Waldo to a walk.\n")

play = "yes"
while play == "yes":
    print("Here we have some places where we can take Waldo:\n")

    # Printing the list of pictures
    for index, place in enumerate(backgrounds):
        print(f"{index} - {place}")

    selected_image = -1
    # Ask the user to select an image
    while selected_image not in range (0, 5):
        selected_image = int(input("\nPlease, type the number corresponding to the place you want to use: ") or -1)
    
    print("Working in the selected image, please wait a while...")
    image_background = Image.open(f"{images_path}{backgrounds[selected_image]}")
    pixels_background = image_background.load()

    # Image with a green background we will use to put at the chosen background
    image_item = Image.open("images/waldo.jpg")
    pixels_item = image_item.load()
    width_item, height_item = image_item.size

    # Creating a new image with same dimensions of our image_item
    image_new = Image.new("RGB", image_item.size)
    pixels_new = image_new.load()

    # Working the images    
    for column in range (0, width_item):
        print(f".", end="")
        for row in range (0, height_item):
            #print(f"[{column}, {line}]")
            r, g, b = pixels_item[column, row]

            if r < 100 and (g > 200 and g < 211) and b < 100:
                pixels_new[column, row] = pixels_background[column, row]
            else:
                #print(f"r: {r} g: {g} b: {b}")
                pixels_new[column, row] = pixels_item[column, row]
    
    print("\nDone!")

    # Saving the new image
    path_file_name = f"{images_path}{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{backgrounds[selected_image]}"
    image_new.save(path_file_name)
    print(f"\nNew image saved at {path_file_name}")

    # Attempting to open a new window to display the image.
    image_new.show()
    
    play = (input("\nDo you want try again? Type yes or no: ").lower() or "no")

print(f"{line}*     Thanks for use the Looping Activity    *{line}")