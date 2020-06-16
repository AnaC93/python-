my_string = input('Type your sentence here: ')
my_list = my_string.split()
for ind, word in enumerate(my_list):
    print(ind + 1, word)