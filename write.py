from openpyxl import load_workbook
from load import loadData

doc = load_workbook(filename='CPH_KEA sep2019-1.xlsx')
ws = doc.active

result = loadData()

columns = 0
for col in ws.iter_rows(min_col=7, max_col=7, min_row=2):
    for cell in col:
        cell.value = result[columns]
        columns = columns + 1


doc.save('CPH_flykoder_opdateret.xlsx')
