import pandas as pd
df = pd.ExcelFile("trekking1.xlsx").parse()

df_sorted = df.sort_values(by=['ККал на 100', 'Unnamed: 0'], ascending=[False, True])
print(df_sorted)