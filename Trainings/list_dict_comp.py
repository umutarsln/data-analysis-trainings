import seaborn as sns

df = sns.load_dataset("car_crashes")

#df.columns = [col.upper() for col in df.columns]

#print(df.columns)

df.columns = ["_".join(["FLAG",col]) for col in df.columns]

print(df.columns)