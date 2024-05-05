import pandas as pd
    
#Read the .csv file provided by TravelPerk
df = pd.read_csv('./data/hackupc-travelperk-dataset.csv')
#Format the date columns
df['Departure Date'] = pd.to_datetime(df['Departure Date'], format="%d/%m/%Y")
df['Return Date'] = pd.to_datetime(df['Return Date'], format="%d/%m/%Y")


def getTravelers(date, city):
    """These function filter the dataframe given by Travelperk wich simulates a fake database
    of future trips. The filter conditions are the trip dates and the arraival city. It returns
    a json doc with the users who can match in their final destinations in the same dates.

    Args:
        date (str): the date of arrival to de destination
        city (str): the destination city

    Returns:
        .json: a json file with all the matches
    """
    global df
    date = pd.to_datetime(date, format="%d/%m/%Y")
    
    dateFiltered = df[(date >= df['Departure Date']) & (date <= df['Return Date'])]
    dateFiltered.loc[:, 'Departure Date'] = dateFiltered['Departure Date'].astype(str)
    dateFiltered.loc[:, 'Return Date'] = dateFiltered['Return Date'].astype(str)
    
    locFilter = dateFiltered[city.lower() == dateFiltered['Arrival City'].str.lower()]
    
    return locFilter.to_json(orient='records', lines=True)