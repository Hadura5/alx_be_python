
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))


monthly_savings = monthly_income - monthly_expenses


annual_interest_rate = 0.05
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)


print(f"Monthly Savings: ${monthly_savings:.2f}")
print(f"Projected Annual Savings (including 5% interest): ${projected_savings:.2f}")
