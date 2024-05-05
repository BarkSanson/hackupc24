import pandas as pd
import datetime as dt
    
#Read the .csv file provided by TravelPerk
df = pd.read_csv('../../../hackupc-travelperk-dataset.csv')
#Format the date columns
df['Departure Date'] = pd.to_datetime(df['Departure Date'], format="%d/%m/%Y")
df['Return Date'] = pd.to_datetime(df['Return Date'], format="%d/%m/%Y")


def getTravelersByMonth(date):
    global df
    date = pd.to_datetime(date, format="%d/%m/%Y")
    
    filtered = df[(date >= df['Departure Date']) & (date <= df['Return Date'])]
    filtered['Departure Date'] = filtered['Departure Date'].astype(str)
    filtered['Return Date'] = filtered['Return Date'].astype(str)
    
    return filtered.to_json(orient='records', lines=True)
            
        
    