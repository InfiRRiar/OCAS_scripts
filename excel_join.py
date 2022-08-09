import pandas as pd

# объединяет 2 excel файла в один (УНИВЕРСАЛЬНЫЙ)
original = pd.read_excel("Import/Import.xlsx", sheet_name="Лист1", header=None)
join = pd.read_excel("Import/nofaq.xlsx", sheet_name="Лист1", header=None)

e_dict = {"0": [],
          "1": []}
for i in range(len(original)):
    if not pd.isnull(original.iloc[i][1]):
        e_dict["0"].append(original.iloc[i][0])
        e_dict["1"].append(original.iloc[i][1])
    
for i in range(len(join)):
    if not pd.isnull(join.iloc[i][1]):
        if str(join.iloc[i][0]) == "0":
            e_dict["0"].append("")
        else:
            e_dict["0"].append(join.iloc[i][0])
        e_dict["1"].append(join.iloc[i][1])

original = pd.DataFrame(e_dict)
original.to_excel("Export/IMPORT.xlsx", index=False, header=False)