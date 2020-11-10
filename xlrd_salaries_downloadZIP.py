import xlrd
salaries_dic = {}

for i in range(1, 1001):
    rb = xlrd.open_workbook(rf'C:\Users\Slam\PycharmProjects\xlrd_xlwr_students\rogaikopyta\{i}.xlsx',)
    sheet = rb.sheet_by_index(0)
    row = sheet.row_values(1)
    for c_el in row[1:4:2]:
        salaries_dic[row[1]] = row[3]
        print(c_el, end=' ')
    print()

for fio, dig in sorted(salaries_dic.items()):
    print(fio, int(dig))







