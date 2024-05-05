import pandas as pd
import datetime as dt
    
#Read the .csv file provided by TravelPerk
df = pd.read_csv('../../../hackupc-travelperk-dataset.csv')
#Format the date columns
df['Departure Date'] = pd.to_datetime(df['Departure Date'], format="%d/%m/%Y")
df['Return Date'] = pd.to_datetime(df['Return Date'], format="%d/%m/%Y")


def getTravelers(date, city):
    global df
    date = pd.to_datetime(date, format="%d/%m/%Y")
    
    dateFiltered = df[(date >= df['Departure Date']) & (date <= df['Return Date'])]
    dateFiltered.loc[:, 'Departure Date'] = dateFiltered['Departure Date'].astype(str)
    dateFiltered.loc[:, 'Return Date'] = dateFiltered['Return Date'].astype(str)
    
    locFilter = dateFiltered[city.lower() == dateFiltered['Arrival City'].str.lower()]
    
    return locFilter.to_json(orient='records', lines=True)