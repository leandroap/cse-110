# 02-Activity_IDBadge_LAP.py
# Author: Leandro Amaral Pereira

print("Please enter the following information:\n")

first_name = input("First name: ").capitalize()
last_name = input("Last name: ").upper()
email = input("Email address: ").lower()
phone_number = input("Phone number: ")
job_title = input("Job title: ").capitalize()
id_number = input("ID number: ")

hair_color = input("Hair color: ")
eyes_color = input("Eyes color: ")
month_started = input("What month did you started? ")
training = input("Did you finish the advanced training? (yes/no): ").capitalize()

hair_eyes = f"Hair: {hair_color : <15} Eyes: {eyes_color}"
month_training = f"Month: {month_started : <15}Training: {training}"

stretch_output = f"{hair_eyes}\n{month_training}"

print("\nThe ID Card is:")

output = f"----------------------------------------\n{last_name}, {first_name}\n{job_title} \nID: {id_number}\n\n{email}\n{phone_number}\n\n{stretch_output}\n----------------------------------------"

print(output)