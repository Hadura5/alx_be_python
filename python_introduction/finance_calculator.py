monthly_income = int(input ("enter your monthly income:"))

total_monthly_expenses = int(input ("enter your total monthly expenses?"))

  monthly_savings = monthly_income - total_monthly_expenses
  annual_interest_rate = 0.05
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 + 0.05)

print(f"Monthly Savings: ${monthly_savings:.2f}")
print(f"Projected Annual Savings (including 5% interest): ${projected_savings:.2f}")
