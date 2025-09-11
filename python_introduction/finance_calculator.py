# Objective: To calculate monthly and projected annual savings based on user input.

# 1. Get user input for financial details.
# The input() function gets user input as a string.
monthly_income_str = input("Enter your monthly income: ")
monthly_expenses_str = input("Enter your total monthly expenses: ")

# 2. Convert input strings to floating-point numbers for calculations.
monthly_income = float(monthly_income_str)
monthly_expenses = float(monthly_expenses_str)

# 3. Calculate monthly savings by subtracting expenses from income.
monthly_savings = monthly_income - monthly_expenses

# 4. Assume a simple annual interest rate of 5% (0.05).
annual_interest_rate = 0.05

# 5. Calculate the projected savings after one year, including interest.
# Formula: (Monthly Savings * 12) + (Monthly Savings * 12 * 0.05)
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# 6. Display the results in the specified format.
# The f-string format is used to easily embed variables into strings.
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
