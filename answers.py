import json
import pandas as pd

dict = {}
file = pd.read_excel("Dataset.xls", sheet_name="Ответы на матрицу")
for i in range(20):
    dict[i + 1] = {}
    for j in range(1, 33):
        if pd.isnull(file.iloc[i][j]):
            dict[i + 1][j] = "Error: no answer was found"
        else:
            dict[i + 1][j] = file.iloc[i][j]
with open("Export/answers.json", "w") as write_file:
    json.dump(dict, write_file, ensure_ascii=False)
