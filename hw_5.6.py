dict = {}
with open("text.txt", encoding='utf=8') as file:
    for line in file:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        dict[name] = name_sum

print(f"{dict}")