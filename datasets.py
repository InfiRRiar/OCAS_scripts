import pandas as pd

file = pd.read_excel("Dataset.xls", sheet_name="Ограниченная  матрица")
e_dict = {"id" :[],
          "object": []}
for i in range(300):
    for j in range(1, 33):
        if pd.isnull(file.iloc[i][j]):
            continue
        else:
            id_1 = i
            id_1 = id_1 // 15 + 1
            e_dict["id"].append(str(id_1) + " " + str(j + 1000))
            e_dict["object"].append(file.iloc[i][j])
exp = pd.DataFrame(e_dict)
exp.to_excel("Export/dataset.xls", index=False)