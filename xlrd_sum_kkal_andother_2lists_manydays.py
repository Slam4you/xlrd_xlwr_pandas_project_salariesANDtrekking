import xlrd
rb = xlrd.open_workbook('trekking3.xlsx')
sheet = rb.sheet_by_index(0)
Kkal = {}


rb = xlrd.open_workbook('trekking3.xlsx')
day_racion = rb.sheet_by_index(1)
day_racion_dic = {}
racion_kkal_total = 0
racion_B_total = 0
racion_J_total = 0
racion_Y_total = 0
count_days = 1

for row_num in range(1, sheet.nrows):
    row = sheet.row_values(row_num)
    for c_el in row[0:1]:
        for i in range(1, 5):
            if row[i] == '':
                row[i] = 0
        Kkal[c_el] = [row[1], row[2], row[3], row[4]]
print(Kkal)

for row_num in range(1, day_racion.nrows):
    row = day_racion.row_values(row_num)
    for c_el in row[1:2]:
        if row[0] == count_days:
            day_racion_dic[c_el] = [row[2]]
            if c_el in Kkal:
                racion_kkal_total += Kkal[c_el][0] / 100 * day_racion_dic[c_el][0]
                racion_B_total += Kkal[c_el][1] / 100 * day_racion_dic[c_el][0]
                racion_J_total += Kkal[c_el][2] / 100 * day_racion_dic[c_el][0]
                racion_Y_total += Kkal[c_el][3] / 100 * day_racion_dic[c_el][0]
        else:
            print(int(racion_kkal_total), int(racion_B_total), int(racion_J_total), int(racion_Y_total))
            racion_kkal_total = 0
            racion_B_total = 0
            racion_J_total = 0
            racion_Y_total = 0
            count_days += 1
            day_racion_dic[c_el] = [row[2]]
            if c_el in Kkal:
                racion_kkal_total += Kkal[c_el][0] / 100 * day_racion_dic[c_el][0]
                racion_B_total += Kkal[c_el][1] / 100 * day_racion_dic[c_el][0]
                racion_J_total += Kkal[c_el][2] / 100 * day_racion_dic[c_el][0]
                racion_Y_total += Kkal[c_el][3] / 100 * day_racion_dic[c_el][0]

print(day_racion_dic)
print(int(racion_kkal_total), int(racion_B_total), int(racion_J_total), int(racion_Y_total))
