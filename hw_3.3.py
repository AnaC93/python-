def my_func():
    x = int(input('Enter the int: '))
    y = int(input('Enter the int: '))
    z = int(input('Enter the int: '))
    min(x, y, z)
    result = x + y + z - min(x, y, z)
    print(result)


my_func()