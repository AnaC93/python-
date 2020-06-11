rev = int(input("Enter your total revenue: "))
cost = int(input("Enter your total costs: "))
if rev > cost:
    print("Profit with", rev / cost, "financial viability")
    employee = int(input("Enter the number of your employees: "))
    individual_profit = (rev - cost) / employee
    print(individual_profit, "$", "per employee")
else:
    print("Loss")