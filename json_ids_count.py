import json

# Кол-во строк на каждый АЙДИШНИК
file = json.load(open("Import/test.json"))
dict = dict()
for i in list(file.keys()):
    dict[i] = len(file[i])
with open("Export/ids_count.txt", "w") as file:
    res = []
    for i in list(dict.keys()):
        res.append(str(i) + " - " + str(dict[i]) + "\n")
    file.writelines(res)
file.close()
print(dict)
