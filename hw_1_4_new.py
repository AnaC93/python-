number = input("Enter the number: ")
start_value = 0
max_value = 0
while start_value < len(number):
    if int(number[start_value]) > max_value:
        max_value = int(number[start_value])
    start_value = start_value + 1

print(max_value)