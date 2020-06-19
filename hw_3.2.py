def user_info(**kwargs):
    return kwargs

print(user_info(
    name=input('Enter your name: '),
    sur=input('Enter your surname: '),
    year=input('Enter your birth year: '),
    city=input('Enter your city: '),))


