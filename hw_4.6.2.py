from itertools import cycle

my_list = [1, 2, 3, 4, 5]
count = 0
for el in cycle(my_list):
    if count > 19:
        break
    print(el)
    count += 1