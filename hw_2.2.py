a = input('Enter an int: ')
b = input('Enter an int: ')

new_list = [a, b]
#print(new_list)

print(a, b)

a, b = b, a
print(a, b)