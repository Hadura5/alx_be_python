monthly_income = float(input ("enter your monthly income?"))

monthly_expenses = float(input ("enter your total monthly savings?"))

interest = 0.05 
monthly_savings = monthly_income - monthly_expenses
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 + 0.05)

print ( f"your monthly savings are {monthly_savings}")
print (f"your projected savings after one year, with interest, is : {projected_annual_savings}")
