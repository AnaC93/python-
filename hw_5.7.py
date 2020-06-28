import json

result = []
with open("text.json", "w", encoding="utf-8") as write_f:
    with open("text.txt", encoding="utf-8") as f_obj:
        profit = {}
        for line in f_obj:
            profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        average = sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0])
        result.append(profit)
        result.append({"average is": round(average)})
    json.dump(result, write_f)