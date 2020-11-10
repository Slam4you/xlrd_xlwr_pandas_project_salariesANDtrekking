import xlrd
import statistics

rb = xlrd.open_workbook('salaries.xlsx')
sheet = rb.sheet_by_index(0)

mediana_city_max = 0
city_name_max_mediana =''
salary_prof_max = 0
salary_name_prof_max =''
for row_num in range(1, sheet.nrows):
    row = sheet.row_values(row_num)
    mlist = []                                          # Создаёт и обнуляет пустой лист для подсчёта медианы ЗП по городам
    for c_el in row[1:]:
        print(c_el, end=' / ')
        mlist.append(float(c_el))                       # Добавление в лист ЗП для подсчёта медианы по городам
    if statistics.median(mlist) > mediana_city_max:     # Если медиана больше чем ранее перебранная => запоминаем город и значение
        mediana_city_max = statistics.median(mlist)
        city_name_max_mediana = row[0]
    print()
    print(statistics.median(mlist))

for col_num in range(1, sheet.ncols):
    column = sheet.col_values(col_num)
    mlist = []
    for r_el in column[1:]:
        print(r_el, end=' / ')
        mlist.append(float(r_el))
    if sum(mlist)/len(mlist) > salary_prof_max:
        salary_prof_max = sum(mlist)/len(mlist)
        salary_name_prof_max = column[0]
    print()



print('Max meridian city:', city_name_max_mediana)
print('Max prof sred:', salary_name_prof_max)