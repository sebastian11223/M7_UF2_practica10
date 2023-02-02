import pandas as pd
import datetime as dt
lector = pd.read_csv("df_covid19_countries.csv")
df = pd.DataFrame(lector)


#if df[['location']]:
#print(df.loc[df['location']=='Afghanistan'])
#print(df[['location']])

#def MostrarCasos():
#print(df.loc[df['location']=='Albania'] & (df.date.isin(['2020-02-24','2020-12-31'])))
#print(df.loc[df['location']=='Albania'])
#print(df.loc[df['date'] == '2020-02-24'])





#print(df.loc[df['location'] == 'Afghanistan'])
#print(df.loc[df['location'] == 'Albania'])
#print(df.loc[df['location'] == 'Algeria'])
#print(df.loc[df['location'] == 'Armenia'])
#print(df.loc[df['location'] == 'Barbados'])
#print(df.loc[df['location'] == 'Bulgaria'])
#print(df.loc[df['location'] == 'Comoros'])
#print(df.loc[df['location'] == 'Denmark'])
#print(df.loc[df['location'] == 'Falkland'])
#print(df.loc[df['location'] == 'France'])




lector['date'] = pd.to_datetime(lector.date)


#df['sum'] = df.loc[df['x'] > 0,['x','y']].sum(axis=1)
#lector['date'] = pd.Series(pd.date_range("2020-02-24", "2020-12-31").sum())

fechas = pd.Series(pd.date_range("2020-02-24", "2020-12-31"))
df['date'] = pd.to_datetime(df.date)



mes = df['date'].dt.month.head(10)

mes1 = df['date'].dt.month
afg = df['location'] == 'Afghanistan'

casos = df.groupby([afg, mes1])['total_cases'].sum()

#print(fechas)
print(casos)

#MostrarCasos()