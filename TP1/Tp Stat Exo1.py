import pandas as pd
import numpy as np

datab = {'X':[78,85,96,80,86,55,43],
         'Y':[84,84,89,83,86,39,68],
         'Z':[86,97,96,72,83,87,95]}
#Qst1
df1= pd.DataFrame(datab)

#Qst 2
df2 = df1.loc[[1,3,4,5,6],['X','Z']]
print(df2)

#Qst 3
print(df1[df1['Y']== 84])
#Qst 4
print(df2.count(axis=1),df2.count(axis=0))
print("Lignes: ",len(df2.count(axis=1)),'\nColonnes: ',len(df2.count(axis=0)))
#Qst 5
print(df1[(df1['Z'] <= 90) & (df1['Z'] >= 75)])
#Qst 6
df1.iloc[3,]=[11,12,13]
print(df1)
#Qst 7
df1.loc[7,]= [15,16,17]
print(df1)
#Qst 8
df1 = df1.sort_values(by=['Y','X'],ascending=True)
print(df1)

print(df1['Y'].unique())