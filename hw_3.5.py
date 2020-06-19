def number_sum():
    exit = False
    result = 0
    while exit == False:
        numbers = input('Enter the numbers or @ to exit: ').split()
        interm_res = 0
        for num in numbers:
            if '@' in num:
                exit = True
                break
            interm_res += int(num)
        result += interm_res
    print(result)


number_sum()