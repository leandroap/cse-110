# Week 12 Prove: Assignment Milestone
# Analyze a dataset about life expectancies 
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse110-course/lesson11/prove.html

# Function to print some decorative elements
def print_elements(option): 
    break_line = "\n***********************************************\n"
    header       = "*   Welcome to the Data Analysis Program!     *"
    footer       = "*  Thanks for use the Data Analysis Program!  *"

    if option == "header":
        print(f"{break_line}{header}{break_line}")
    elif option == "footer":
        print(f"{break_line}{footer}{break_line}")

entity_list = []
code_list = []
year_list = []
life_expectancy_list = []

interest_entity_list = []
interest_year_list = []
interest_life_expectancy_list = []

country_year_list = []
country_life_expectancy_list = []

print_elements("header")

interest_year = input("Enter the year of interest: ")
country = input("Enter a country of interest: ").capitalize()

# Load the dataset in your Python program
with open("resources/life-expectancy.csv") as life_expectancy_file:
    # Skip HEADER LINE: Entity,Code,Year,Life expectancy (years)
    next(life_expectancy_file)

    # Iterate through the data line by line
    for i, line in enumerate(life_expectancy_file):
        # Split each line into parts
        line = line.strip()
        entity, code, year, life_expectancy = line.split(",")

        # Save values into lists to analyze them
        entity_list.append(entity)
        code_list.append(code)
        year_list.append(year)
        life_expectancy_list.append(float(life_expectancy))

        #Working with the interest year data
        if year == interest_year:
            interest_entity_list.append(entity)
            interest_year_list.append(year)
            interest_life_expectancy_list.append(float(life_expectancy))

        #Working with the interest country data
        if entity == country:
            country_year_list.append(year)
            country_life_expectancy_list.append(float(life_expectancy))

# Find the lowest and the highest value for life expectancy in the dataset.
index_max = life_expectancy_list.index(max(life_expectancy_list))
index_min = life_expectancy_list.index(min(life_expectancy_list))

print("\nIn the whole dataset:")
print(f"- The overall max life expectancy is: {life_expectancy_list[index_max]} from {entity_list[index_max]} in {year_list[index_max]}")
print(f"- The overall min life expectancy is: {life_expectancy_list[index_min]} from {entity_list[index_min]} in {year_list[index_min]}")

print(f"\nFor the year {interest_year}:")
if interest_entity_list:
    # Find the average, the lowest and the highest value for life expectancy in the dataset for the interest year.
    index_max = interest_life_expectancy_list.index(max(interest_life_expectancy_list))
    index_min = interest_life_expectancy_list.index(min(interest_life_expectancy_list))
    interest_average = sum(interest_life_expectancy_list) / len(interest_life_expectancy_list)

    print(f"- The average life expectancy across all countries was {interest_average:.2f}")
    print(f"- The max life expectancy was in {interest_entity_list[index_max]} with {interest_life_expectancy_list[index_max]}")
    print(f"- The min life expectancy was in {interest_entity_list[index_min]} with {interest_life_expectancy_list[index_min]}")
else:
    print(f"- Any data was found for the year {interest_year}.")

if country_life_expectancy_list:
    # Find the average, the lowest and the highest value for life expectancy in the dataset for the interest year.
    index_max = country_life_expectancy_list.index(max(country_life_expectancy_list))
    index_min = country_life_expectancy_list.index(min(country_life_expectancy_list))
    country_average = sum(country_life_expectancy_list) / len(country_life_expectancy_list)

    print(f"\nFor the country {country}:")
    print(f"- The average life expectancy for the country is {country_average:.2f}")
    print(f"- The max life expectancy was in {country_year_list[index_max]} with {country_life_expectancy_list[index_max]}")
    print(f"- The min life expectancy was in {country_year_list[index_min]} with {country_life_expectancy_list[index_min]}")
else:
    print(f"\nFor the country {country}:")
    print(f"- Any data was found for the country {country}.")

print_elements("footer")