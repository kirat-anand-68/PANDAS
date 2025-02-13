import pandas as pd
df=pd.read_csv('data.csv')
df.head(5)
df.isnull().head(5)
df.isnull().sum()
df_filled=df.fillna(0)
print(df_filled)

# df['New-values']=df['Value'].apply(lambda x:x*2)
grouped_mean=df.groupby('product')['Value'].mean()
print(grouped_mean)
