import openpyxl

files = ['1111.xlsx', '2222.xlsx', '3333.xlsx']

data_list = []

for file in files:
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active
    for row in sheet.iter_rows(values_only=True):
        data_list.append(row)

sorted_data = sorted(data_list, reverse=True)

for row in sorted_data:
    print(row)
