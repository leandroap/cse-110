# File: 06-Check_QualifyingLoan.py
# Author: Leandro Amaral Pereira
# Purpose: Qualifying for a Loan
# Reference: https://byui-cse.github.io/cse110-course/lesson06/checkpoint.html

print("Please, type a rating from 1-10 on the following questions:\n")

loan_size = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income_size = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

is_approved = False

if loan_size >= 5:
    if credit_history >= 7 and income_size >= 7:
        is_approved = True
    elif (credit_history >= 7 or income_size >= 7) and down_payment >= 5:
        is_approved = True
else:
    if credit_history >= 4 and (income_size >= 7 or down_payment >= 7):
        is_approved = True
    elif credit_history >= 4 and income_size >= 4 and down_payment >= 4:
        is_approved = True

print(f"\nYour loan request {('is' if is_approved else 'is not')} approved.\n\n")

print(f"Loan size: {loan_size}, Credit: {credit_history}, Income: {income_size}, Down Payment: {down_payment}, Decision: {('Yes' if is_approved else 'No')}")