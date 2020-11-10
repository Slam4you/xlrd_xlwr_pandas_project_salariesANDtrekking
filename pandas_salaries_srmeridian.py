import pandas as pd
xls = pd.read_excel("salaries.xlsx")
print(xls)
print(xls.median(axis=1))
print(xls.mean(axis=0))