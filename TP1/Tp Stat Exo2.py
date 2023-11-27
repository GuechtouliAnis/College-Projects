import numpy as np
import pandas as pd
import random

n = 7
item = 'Boston Celtics'  # Replace 'your_item' with the actual item you want to repeat

Team_list = [item] * n

Datab = {"Name": ["Avery Bradley","Jae Crowder","John Holland","R.J.Hunter",
                "Jonas Jerebko","Amir Johnson","Jordan Mickey"],
         "Team": Team_list,
         "Number": [0.0,99,30,28,8,90,55],
         "Position": ["PG","SF","SG","SG","PF","PF","PF"],
         "Age": [25,25,27,22,29,29,21],
         "Height": ['6-2','6-6','6-5','6-5','6-10','6-9','6-8'],
         "Weight":[180,235,205,185,231,240,235],
         "College":["Texas","Marquette","Boston University","Georgia Stat",
                    np.nan,np.nan, "LSU"],
         "Salary":[7730337.0,6796117.0,np.nan,1148640.0,5000000.0,
                    12000000.0,1170960.0]}
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', 1000)
#Qst 1
df = pd.DataFrame(Datab)
print(df)

#Qst 2
lists = []
for i in range(df.shape[0]):
    a = random.randint(50,150)
    lists.append(a)
df["points"] = lists
print(df)
print("--------------------------------------------------")
#Qst 3
df.loc[df.shape[0]] = ["Marcus smart","Boston Celtics",36,"PG",22,"6-4",22,"Oklahoma Sate",34310440,50]
print(df)

#Qst 4
df_b = df[df["Name"] == "Avery Bradley"]
print(df_b.loc[:,["Name","Age","Team","Position"]])
# OR
df_b_op = df.loc[df['Name'] == 'Avery Bradley', ['Name', 'Age', 'Team', 'Position']]
print(df_b_op)

#Qst 5
mean_age = df["Age"].mean()
mean_weight = df["Weight"].mean()
mean_salary = df["Salary"].mean()
mean_points = df["points"].mean()

mean_vect = [mean_age,mean_weight,mean_salary,mean_points]
print(mean_vect)

print("--------------------------------")
print(df.describe())