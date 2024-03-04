import pandas as pd

# 12
# Создает файл a_ids из датасета. НЕ УНИВЕРСАЛЬНЫЙ
file = pd.read_excel("Import/Import.xlsx", sheet_name="Лист1")
e_dict = {"id": [],
          "object": []}
names = file.columns.values.tolist()
for i in range(len(file.iloc[0])):
    if not pd.isnull(file.iloc[1][names[i]]):
        e_dict["id"].append(str(names[i]))
        e_dict["object"].append(file.iloc[0][names[i]])

'''file = pd.read_excel("Import/ans_import.xlsx", sheet_name="ответы пользователя")
names = file.columns.values.tolist()
for i in range(len(file.iloc[0])):
    if not pd.isnull(file.iloc[1][names[i]]):
        e_dict["id"].append("A" + str(names[i]))
        e_dict["object"].append("Ответ: " + file.iloc[0][names[i]])'''

exp = pd.DataFrame(e_dict)
exp.to_excel("Export/a_ids.xlsx", index=False, header=False)
