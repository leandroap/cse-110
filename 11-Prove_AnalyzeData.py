# Week 11 Prove: Assignment Milestone
# Analyze a dataset about life expectancies 
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse110-course/lesson11/prove.html

entity_list = []
code_list = []
year_list = []
life_expectancy_list = []

# Load the dataset in your Python program
with open("resources/life-expectancy.csv") as life_expectancy_file:
    # Iterate through the data line by line
    for i, line in enumerate(life_expectancy_file):
        if i == 0:
            #HEADER LINE: Entity,Code,Year,Life expectancy (years)
            print()
        else:
            # Split each line into parts
            line = line.strip()
            entity, code, year, life_expectancy = line.split(",")

            # Save values into lists to analyze them
            entity_list.append(entity)
            code_list.append(code)
            year_list.append(year)
            life_expectancy_list.append(life_expectancy)

# Find the lowest value for life expectancy and the highest value for life expectancy in the dataset.
index_max = life_expectancy_list.index(max(life_expectancy_list))
index_min = life_expectancy_list.index(min(life_expectancy_list))

print(f"The overall max life expectancy is: {life_expectancy_list[index_max]} from {entity_list[index_max]} in {year_list[index_max]}")
print(f"The overall min life expectancy is: {life_expectancy_list[index_min]} from {entity_list[index_min]} in {year_list[index_min]}")

#interest_year = input("Enter the year of interest: ")

#print(f"\nFor the year {interest_year}:")
#print(f"The average life expectancy across all countries was 54.95")
#print(f"The max life expectancy was in Norway with 73.49")
#print(f"The min life expectancy was in Mali with 28.077")