import json
import pandas as pd

# Делает из эксельки с ответами json с ответами
dict = {}
file = pd.read_excel("Import/train.xlsx", sheet_name="Лист1")
print(file)
for i in range(len(file)):
    if str(file.iloc[i][0]).strip() not in dict.keys():
        dict[str(file.iloc[i][0]).strip()] = []
    dict[str(file.iloc[i][0]).strip()].append(file.iloc[i][1])

with open("Export/answers.json", "w") as write_file:
    json.dump(dict, write_file, ensure_ascii=False)