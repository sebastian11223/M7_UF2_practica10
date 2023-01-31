import pandas as pd

leer = pd.read_csv("List of cities proper by population density11.csv", usecols=["City", "Population"] ).head()

df = pd.DataFrame(leer)

#def PerciutatTotalPoblacio(ciutat):
    #result = df['City'] == ciutat
#result = pd.read_csv("List of cities proper by population density11.csv", columns=["Population"])
#print(result)
#ciudad = df.loc[df['City'] == 'Mandaluyong']
#popula = df.loc[df['Population'] == '1,846,513']

#print(df.loc[df['City'] == 'Mandaluyong'])
#print(df.loc[df['Population'] == '1,846,513'])
print(leer)
#print(leer)

#print(pd.concat([ciudad,popula]))


#print(leer)

#print(PerciutatTotalPoblacio())