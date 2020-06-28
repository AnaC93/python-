russian = {"one": "один", "two": "два", "three": "три", "four": "четыре"}

with open("text_1.txt", "a", encoding='utf-8') as new_file:
    with open("text_2.txt", "a", encoding='utf-8') as my_file:
        line = my_file.read().split("\n")
        for i in line:
            i = i.split(" - ")
            new_file.writelines(russian[i[0]] + ' - ' + i[1] + "\n")
        