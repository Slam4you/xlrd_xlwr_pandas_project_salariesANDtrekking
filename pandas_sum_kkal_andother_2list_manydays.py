import pandas as pd
df1 = pd.ExcelFile('trekking3.xlsx').parse('Справочник')
df2 = pd.ExcelFile('trekking3.xlsx').parse('Раскладка')

df2 = df2.merge(df1, left_on='Продукт', right_on='Unnamed: 0').drop(columns=['Unnamed: 0']).fillna(0)
df2['К']=df2['Вес в граммах']*df2['ККал на 100']/100
df2['Б']=df2['Вес в граммах']*df2['Б на 100']/100
df2['Ж']=df2['Вес в граммах']*df2['Ж на 100']/100
df2['У']=df2['Вес в граммах']*df2['У на 100']/100
df2 = df2.loc[:,['День','Вес в граммах','К','Б','Ж','У']]

df_agg = df2.groupby(by=["День"]).sum()
df_agg[['К','Б','Ж','У']] = df_agg[['К','Б','Ж','У']].astype(int)

for row in df_agg.itertuples():
    print(row[2],row[3],row[4],row[5])