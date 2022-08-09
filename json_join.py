import json

# Объединение джейсонов
file = json.load(open("Export/answers.json"))
file1 = json.load(open("Export/answers1.json"))
for i in list(file1.keys()):
    if str(i).strip() not in list(file.keys()):
        file[str(i).strip()] = []
    for j in file1[i]:
        file[str(i).strip()].append(j)
with open("Import/test.json", "w") as write_file:
    json.dump(file, write_file, ensure_ascii=False)
