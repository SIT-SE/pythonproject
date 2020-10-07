import pandas as pd
url = 'https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.xlsx'
df = pd.read_excel(url, header=0)

#df = pd.read_excel (r'C:\Users\jiaji\Downloads\owid-covid-data.xlsx')

# removing locations named 'World' & 'International' as they do not exist.
df = df.drop(df[(df.location =='World') & (df.location =='International')].index)
#removing as data in these columns are assumed that testing changed equally on a daily basis over any periods in which no data was reported.
df.drop(df.columns[[6, 9, 12,15,20,21]], axis = 1, inplace = True)
#replacing NaN with 0 as there were no reports published on that day. Hence, treated as 0 cases.
df.fillna(0, inplace=True)
df.to_excel("covid.xlsx",index=False)
