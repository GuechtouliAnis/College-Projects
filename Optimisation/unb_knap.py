from itertools import product
import numpy as np
import pandas as pd


items = {"Hammer":[11,3], "Screw":[4,2],"Towel":[8,5],"Wrench":[3,7],"Screwdriver":[6,4]}
df = pd.DataFrame(items, index=["Value","Weight"])

st = []
for i in df.columns:
    mod = 15 / df.loc["Weight", i]
    r = range(int(mod)+1)
    st.append(list(r))

# Generate combinations with specific order
combinations = product(*st)

# Filter combinations based on rules
filtered_combinations = []
for combo in combinations:
    valid = True
    for i, val in enumerate(combo):
        if sum(val * df.loc["Weight", df.columns[i]] for i, val in enumerate(combo)) >= 1000:
            valid = False
            break
    if valid:
        filtered_combinations.append(combo)
df_unb = df.copy()

cpt = 1
for comb in filtered_combinations:
    df_unb.loc["pos"+str(cpt)] = comb
    cpt += 1

sums = [df_unb.loc['Value'].sum(),df_unb.loc['Weight'].sum()]
weights = [df_unb.loc['Value'].sum(),df_unb.loc['Weight'].sum()]
for i in range(1,len(df_unb)-1):
    s = 0
    w = 0
    for col in df_unb.columns:
        s += df_unb.loc['pos'+str(i),col] * df_unb.loc['Value',col]
        w += df_unb.loc['pos'+str(i),col] * df_unb.loc['Weight',col]
    sums.append(s)
    weights.append(w)
df_unb['Total Values'] = sums
df_unb['Total Weights'] = weights

dfs_unb = df_unb[df_unb["Total Weights"]<= 15]
dfs_unb.sort_values(by="Total Values",ascending=False).head()