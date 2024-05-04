import pandas as pd

#Read the .csv file provided by TravelPerk
df = pd.read_csv('./res/hackupc-travelperk-dataset.csv')
print(df.head())

#Return a dataframe with all the trips with
def filterByName(df, userName):
    filter = df['Traveller Name'].str.contains(userName, case=False, na=False)
    return df[filter]

#Returns a dataframe with all the trips with the departure date provided
def filterByDepartureDate(df, departureDate):
    filter = df['Departure Date'].str.contains(departureDate, case=False, na=False)
    return df[filter]

def filterByReturnDate(df, returnDate):
    filter = df['Return Date'].str.contains(returnDate, case=False, na=False)
    return df[filter]

def filterByDepartureCity(df, departureCity):
    filter = df['Departure City'].str.contains(departureCity, case=False, na=False)
    return df[filter]

def filterByArrivalCity(df, arrivalCity):
    filter = df['Arrival City'].str.contains(arrivalCity, case=False, na=False)
    return df[filter]