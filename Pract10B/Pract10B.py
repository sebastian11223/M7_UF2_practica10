import pandas as pd
import matplotlib.pyplot as plt

leer = pd.read_csv("List of cities proper by population density11.csv")#, usecols=["City", "Population"] ).head()
df = pd.DataFrame(leer)
def poblaciones():
    df = pd.DataFrame(leer, columns=['City', 'Population'])
    print(df[:10])


def kilometrosCuadrados():
    km = pd.DataFrame(leer, columns=['City', 'Density KM2'])
    print(km[:10])



def MetrosCuadrados():
    leer['Density  M2'] = leer['Density  M2'].replace(',', '.')
    M = pd.DataFrame(leer, columns=['City', 'Density  M2'])
    print(M[:10])

    plt.pie(df["City"])
    plt.title("Ejercicio 2")
    return plt.show()


    plt.pie(leer.City)
    #plt.title("Ejercicio 3")
    plt.show()

MetrosCuadrados()

#def PerciutatTotalPoblacio(ciutat):
    #result = df['City'] == ciutat
#result = pd.read_csv("List of cities proper by population density11.csv", columns=["Population"])
#print(result)
#ciudad = df.loc[df['City'] == 'Mandaluyong']
#popula = df.loc[df['Population'] == '1,846,513']

#print(df.loc[df['City'] == 'Mandaluyong'])
#print(df.loc[df['Population'] == '1,846,513'])
#print(leer)

#print(pd.concat([ciudad,popula]))


#print(leer)

#print(PerciutatTotalPoblacio()))