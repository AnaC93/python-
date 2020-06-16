user_month = int(input('Enter the month number: '))
winter = 'This month is in winter'
winter_list = [12, 1, 2]
spring = 'This month is in spring'
spring_list = [3, 4, 5]
summer = 'This month is in summer'
summer_list = [6, 7, 8]
fall = 'This month is in fall'
fall_list = [9, 10, 11]
if user_month in winter_list:
    print(winter)
if user_month in spring_list:
    print(spring)
if user_month in summer_list:
    print(summer)
if user_month in fall_list:
    print(fall)
if user_month > 12:
    print('There are only 12 months in a year!')