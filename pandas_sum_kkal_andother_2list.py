import pandas as pd

df0 = pd.read_excel('trekking2.xlsx', sheet_name=0)
df1 = pd.read_excel('trekking2.xlsx', sheet_name=1)
df = pd.merge(df0, df1, left_on='Unnamed: 0', right_on='Продукт')

kkal = int(sum((df['ККал на 100'] * df['Вес в граммах'] / 100)))
b = int(sum((df['Б на 100'] * df['Вес в граммах'] / 100)))
zh = int(sum((df['Ж на 100'] * df['Вес в граммах'] / 100)))
u = int(sum((df['У на 100'].fillna(0) * df['Вес в граммах'] / 100)))


print(kkal, b, zh, u)