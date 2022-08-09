import pandas as pd

# Из excel то же самое, но в txt
file = pd.read_excel("Import/train.xlsx", sheet_name="Лист1", header=None)
e_dict = {"id": [],
          "object": []}
with open("Export/all.txt", "w") as result:
    for i in range(len(file)):
        if not pd.isnull(file.iloc[i][0]):
            line = str(int(file.iloc[i][0])) + " - " + str(file.iloc[i][1]) + "\n"
            result.write(line)
result.close()