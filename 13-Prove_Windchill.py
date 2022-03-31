# Week 13 Prove: Assignment
# Wind Chill Calculations
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse110-course/lesson13/prove.html

# Function to print some decorative elements
def print_elements(option): 
    break_line = "\n**********************************************************************\n"
    header       = "*            Welcome to the Wind Chill Calculator Program!           *"
    footer       = "*          Thanks for use the Wind Chill Calculator Program!         *"

    if option == "header":
        print(f"{break_line}{header}{break_line}")
    elif option == "footer":
        print(f"{break_line}{footer}{break_line}")
    elif option == "break_line":
        print(f"{break_line}")

# Function to compute the Wind Chill
def compute_windchill(temperature, wind_speed, type="F"):

    wind_chill = 35.74 + \
        (0.6215 * temperature) - \
            35.75 * (wind_speed ** 0.16) + \
                (0.4275 * temperature) * \
                    (wind_speed ** 0.16)
    
    return wind_chill

# Function to convert celsius to fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * (9/5) + 32)

temperature_entry = None
type_entry = ""

print_elements("header")

# To prevent empty/non numeric entries
while temperature_entry == None:
    try:
        temperature_entry = float(input("What is the temperature? "))
    except:
        temperature_entry = None

# To prevent invalid entries
while type_entry != "F" and type_entry != "C":
    type_entry = (input("Fahrenheit or Celsius (F/C)? ") or "F").upper()
    
    if type_entry == "C":
        temperature_entry = convert_to_fahrenheit(temperature_entry)

print_elements("break_line")

# Loop through wind speeds from 5 to 60 miles per hour
for wind_speed in range(5, 61, 5):
    wind_chill = compute_windchill(temperature_entry, wind_speed, type_entry)
    print(f"At temperature {temperature_entry}F, and wind speed {wind_speed:<2} mph, the windchill is: {wind_chill:6.2f}F")

print_elements("footer")