import numpy as np
import pandas as pd

# Weight of the Backpack is 15
# We have 5 items
# Hammer : Val = 11, Weight = 3
# Screw : Val = 4, Weight = 2
# Towel : Val = 8, Weight = 5
# Wrench : Val = 3, Weight = 7
# Screwdriver : Val = 6, Weight = 4
# First we will do a 0/1 Knapsack

def gen_cases(size):
    cases = []
    for i in range(size):
        binary_string = bin(i)
        binary_string_without_prefix = binary_string[2:]
        cases.append(binary_string_without_prefix)
    for pos in range(len(cases)):
        length = len(cases[-1]) - len(cases[pos])
        if length !=0:
            for i in range(length):
                cases[pos] = "0"+cases[pos]
        else:
            break
    return cases
cases = gen_cases(32)

items = {"Hammer":[11,3], "Screw":[4,2],"Towel":[8,5],"Wrench":[3,7],"Screwdriver":[6,4]}
df = pd.DataFrame(items, index=["Value","Weight"])

df_01 = df.copy()

cpt = 1
for poss in cases:
    f = []
    for n in poss:
        f.append(int(n))
        s = str(cpt)
    df_01.loc["pos"+s]=f
    cpt +=1
sums = [df_01.loc['Value'].sum(),df_01.loc['Weight'].sum()]
weights = [df_01.loc['Value'].sum(),df_01.loc['Weight'].sum()]
for i in range(1,len(df_01)-1):
    s = 0
    w = 0
    for col in df_01.columns:
        s += df_01.loc['pos'+str(i),col] * df_01.loc['Value',col]
        w += df_01.loc['pos'+str(i),col] * df_01.loc['Weight',col]
    sums.append(s)
    weights.append(w)
df_01['Total Values'] = sums
df_01['Total Weights'] = weights

dfs_01 = df_01[df_01["Total Weights"]<= 15]
dfs_01.sort_values(by="Total Values",ascending=False).head()