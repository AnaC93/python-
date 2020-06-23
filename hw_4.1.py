from sys import argv

total, hours, per_hour, bonus = argv

print("Total amount of hours is: ", hours)
print("Rate per hour: ", per_hour)
print("Total bonus is: ", bonus)
print("Total salary is: ", int(hours) * int(per_hour) + int(bonus))
