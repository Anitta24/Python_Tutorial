income = float(input("Enter your income:  "))
if income <= 300000:
    tax = 0
elif income <= 600000:
    tax = 0.05 * (income - 300000)
elif income <= 900000:
    tax = 12500 + 0.1 * (income - 600000)
elif income <= 1200000:
    tax = 75000 + 0.15 * (income - 1200000)
else:
    tax = 187500 + 0.2 * (income - 1500000)
print("Income tax: ", tax)