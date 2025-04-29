import pandas as pandas

df = pd.read_csv('data.csv')

print(df.to_string())

df['Calories'].fillna(300, inplace = True)
df['Maxpulse'].fillna(135, inplace = True)
df['Duration'].fillna(45, inplace = True)
df['Pulse'].fillna(105, inplace = True)