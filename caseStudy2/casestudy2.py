from numpy import dtype
import pandas as pd
import seaborn as sns

df = sns.load_dataset("car_crashes")

#1
#df.columns = [("_".join(["num",col])).upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

#2
#df.columns = [("_".join([col , "flag"])).upper() if "no" not in str(df[col]) else col.upper() for col in df.columns]

#3
"""
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
print(new_df.head())
"""

print(df.columns)





