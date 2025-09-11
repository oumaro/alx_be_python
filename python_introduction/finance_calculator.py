income = int(input("Enter your monthly income:  "))
expenses = int(input("Enter your total monthly expenses: "))y
savings = income - expenses
annual_savings = savings * 12
interest_rate = 0.05
interest_earned = annual_savings * interest_rate

print(f"Projected savings after one year, with interest, is: ${annual_savings}")