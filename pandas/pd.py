import pandas as pd

df = pd.read_csv('pokemon_data.csv')


#print(df.tail(3))

#print(df.columns)

#print(df[['Name', 'HP', 'Type 1']][0:5])

#print(df.iloc[1:4])

print(df.iloc[2,1])