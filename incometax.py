income = float(input("Enter your income:  "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = 0.05 * (income - 250000)
elif income <= 1000000:
    tax = 12500 + 0.1 * (income - 500000)
elif income <= 1500000:
    tax = 75000 + 0.15 * (income - 1000000)
else:
    tax = 187500 + 0.2 * (income - 1500000)
print("Income tax: ", tax)