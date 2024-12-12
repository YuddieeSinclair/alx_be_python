#!/bin/bash
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
savings = monthly_income - monthly_expenses
rate = 0.05
annual_savings =  savings * 12 + (savings * 12 * rate)
print(f"your monthly savings is: {savings}")
print(f"Projected savings after one year, with interest, is:{annual_savings}")
