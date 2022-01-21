# Week 03 Prove: Milestone - Meal Price Calculator
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse110-course/lesson03/prove.html

line = "\n**********************************************\n"

## STRETCH - Welcome message
print(f"{line}*    Welcome to the Meal Price Calculator    *{line}")

## CORE REQUIREMENTS - Questions
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
children_qtd = int(input("How many children are there? "))
adults_qtd = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

## CORE REQUIREMENTS - Values Computing
tax_rate = tax_rate / 100
child_meal_subtotal = child_meal_price * children_qtd
adult_meal_subtotal = adult_meal_price * adults_qtd
subtotal = child_meal_subtotal + adult_meal_subtotal
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax

## STRETCH - style
print(line)

## CORE REQUIREMENTS - Display values with two decimals and $ sign
print(f"Subtotal: ${round(subtotal,2)}")
print(f"Sales Tax: ${round(sales_tax,2)}")
print(f"Total: ${round(total,2)}")

## STRETCH - style
print(line)

## CORE REQUIREMENTS - Payment amount and charge
payment_amount = float(input("What is the payment amount? "))
charge = payment_amount - total

print(f"Change: ${round(charge,2)}\n")

## STRETCH - Goodbye message
print(f"{line}*  Thanks for use the Meal Price Calculator  *{line}")