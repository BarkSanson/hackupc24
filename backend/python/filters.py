def filterByName(df, userName):
    """These function filter the dataframe given by the name of the user, also
    given and return a datafreme with all the trips for the user

    Args:
        df (dataframe): dataframe whith all the fake users
        userName (str): the name to search in the data frame

    Returns:
        dataframe: dataframe with all the trips for userName
    """
    filter = df['Traveller Name'].str.contains(userName, case=False, na=False)
    return df[filter]

def filterByDepartureDate(df, departureDate):
    """These function filter the dataframe given by the departure date, also
    given and return a datafreme with all the trips with these departure dates

    Args:
        df (dataframe): dataframe whith all the fake users
        departureDate (str): date of departure for the trip

    Returns:
        _dataframe: dataframe with all the trips with the date given
    """
    filter = df['Departure Date'].str.contains(departureDate, case=False, na=False)
    return df[filter]

def filterByReturnDate(df, returnDate):
    """These function filter the dataframe given by the return date, also
    given and return a datafreme with all the trips with these return dates

    Args:
        df (dataframe): dataframe whith all the fake users
        returnDate (str): date of return for the trip

    Returns:
        dataframe: dataframe with all the trips with the return date given
    """
    filter = df['Return Date'].str.contains(returnDate, case=False, na=False)
    return df[filter]

def filterByDepartureCity(df, departureCity):
    """These function filter the dataframe given by the departure city, also
    given and return a datafreme with all the trips with these departure location

    Args:
        df (dataframe): dataframe whith all the fake users
        departureCity (str): The departure city of the trip

    Returns:
        dataframe: dataframe with all the trips with the given departure city
    """
    filter = df['Departure City'].str.contains(departureCity, case=False, na=False)
    return df[filter]

def filterByArrivalCity(df, arrivalCity):
    """These function filter the dataframe given by the Arrival city, also
    given and return a datafreme with all the trips with these arrival

    Args:
        df (dataframe): dataframe whith all the fake users
        arrivalCity (str): the arrival citi

    Returns:
        dataframe: dataframe with all the trips with the given arrival city
    """
    filter = df['Arrival City'].str.contains(arrivalCity, case=False, na=False)
    return df[filter]