while True:
    day = 1
    initial_result = int(input("Enter the initial result in km: "))
    expected_result = int(input("Enter the anticipated result: "))
    if initial_result > expected_result:
        print("Wrong data")
    else:
        while initial_result < expected_result:
            initial_result += initial_result * 0.1 #initial_result = initial_result + initial_result * 0.1
            day += 1 #day = day + 1
        print("You'll achieve the anticipated result in {} days".format(day))
        break