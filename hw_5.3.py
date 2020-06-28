with open("text.txt", "r", encoding="utf-8") as my_file:
    sum = []
    less = []
    line = my_file.read().split("\n")
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        sum.append(i[1])

print(f"salary less than 20000 {less}. Average salary - {sum(map(float, sum)) / len(sum)}")