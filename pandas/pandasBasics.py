#2 imp things in pandas are dataframe and series
import pandas as pd
import numpy as np


# import os
# print(os.getcwd())

#creating dataframe using dict
data = {'name':['rahul','om','raj'],'age':[1,2,3]}
# print(data)
df = pd.DataFrame(data)
# print(df)

#series in pandas
series1 = pd.Series([1,2,3])
# print(series1)

series2 = pd.Series([4,5,6],index=['ck','kk','pk'])
# print(series2)

peopleSeries = pd.read_csv("people_data.csv")
# print(peopleSeries)

# print(peopleSeries.head())
# print()
# print(peopleSeries.info())
# print()
# print(peopleSeries.shape)
# print()
# print(peopleSeries.aggregate)
# print()

#renaming the columns
# peopleSeries.rename(columns={"Sex":"Gender"},inplace=True)
# print(peopleSeries.head())

# function isnull()
df = pd.DataFrame({"name":[np.nan,'raj','rohan'],"age":[1,np.nan,3]})
# print(df)
# print(df.isnull())
# df.fillna(0,inplace=True)
# print(df)
# dropping empty rows
# df.dropna(inplace=True)
# print(df)

#filtering column and values of column
age_col = df['age']
# print(age_col)

#only age which is greater than 1
age_col = df[df['age']>1]
# print(age_col)


