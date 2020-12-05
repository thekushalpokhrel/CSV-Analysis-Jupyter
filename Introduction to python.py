import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/user/Downloads/Effects-of-COVID-19-on-trade-1-February-25-November-2020-provisional.csv')

df

print (country_df.head())

country_df = df['country']

df

print (df.head())

print (df.info())

print (country_df.head())

print (df.info())

df_country = df ['Country']

print (df_country.head())

print (df_country.tail())

print(subset.tail)

df_subset = df[['Country', 'Measure','Value']]

print(subset.head())

print(subset.head)

df_subset = df[['Country', 'Measure','Value']]

print(subset.head)

subset = df[['Country', 'Measure','Value']]

print(subset.head())

print(subset.tail())

print(df.loc[0])

print(df.loc[30])

print(df.loc[12])

print(df.tail(n=1))

print(df.tail(n=2))

print(df.tail(n=3))

print(df.loc[[0, 99, 999]])

print(df.iloc[1])

print(df.iloc[33])

print(df.iloc[-1])

print(df.iloc[[0, 99, 999]])

subset = df.loc[:, ['year', 'date']]

subset = df.loc[:, ['Year', 'Date']]

print(subset.head())

print(subset.tail())

subset = df.loc[:, ['Year']]

print(subset.head())

print(subset.tail[0, 99, 999])

print(subset(0, 99, 999))

print(subset.head())

print(subset.tail())

subset = df.loc[:, ['Year' , 'Date']]

subset.head()

subset.tail()

subset = df.iloc[:, [2, 4, -1]]

subset.head()

subset.tail()

