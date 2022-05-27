import pandas as pd

df = pd.read_csv('data.csv')

print(type(df['Calories'][0]))

s = [str(i) for i in pd.Series(df['Calories'])]

for q in range(len(s)):
  df.loc[q, "Calories"] = s[q]

print(pd.Series(df['Calories']), type(df['Calories'][0]))