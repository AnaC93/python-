count = 0
with open("text.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        count += 1
        line_words = line.split()
        print(line, 'String length is: ', len(line_words))
    print("Total amount of strings: ", count)