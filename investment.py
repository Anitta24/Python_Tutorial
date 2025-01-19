initial_investment = float(input("Enter the initial investment:"))
annual_intrest_rate = float(input("Enter the annual intrest rate(in %):"))
year=int(input("Enter the number of years:"))
annual_intrest_rate = annual_intrest_rate/100
print("\nYear\tAmount")
amount=initial_investment
for year in range(1,year+1):
    amount+=amount*annual_intrest_rate
    print(year,"\t","%.2f" % amount)