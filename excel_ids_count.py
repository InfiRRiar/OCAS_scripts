import pandas as pd

# Считает, сколько в файле excel строк на каждый айдишник (УНИВЕРСАЛЬНЫЙ)
file = pd.read_excel("Import/Import.xlsx", sheet_name="Лист1", header=None)
v_all = {}
for i in range(len(file)):
    if file.iloc[i][0] not in list(v_all.keys()):
        v_all[file.iloc[i][0]] = 1
    else:
        v_all[file.iloc[i][0]] += 1
with open("Export/ids_count.txt", "w") as file:
    for i in list(v_all.keys()):
        line = str(i) + " - " + str(v_all[i]) + "\n"
        file.write(line)
file.close()
