import pandas as pd 

pokemon = pd.read_csv('pokemon_data.csv')

pokemon.to_html('edu.html')