import xlrd

rb = xlrd.open_workbook('trekking1.xlsx')
sheet = rb.sheet_by_index(0)
Kkal = {}

for row_num in range(1, sheet.nrows):
    row = sheet.row_values(row_num)
    for c_el in row[0:1]:
        Kkal[c_el] = row[1]

sorted_dic = sorted(sorted(Kkal.items()), key=lambda t: t[1], reverse=True)
for i in sorted_dic:
    print(i[0])



