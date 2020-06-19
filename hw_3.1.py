def my_div():
    x = int(input('Enter the dividend: '))
    y = int(input('Enter the divisor: '))
    try:
        quotient = x // y
        print(quotient)
    except:
        print('Cannot divide by zero!')


my_div()