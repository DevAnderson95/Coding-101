def describe_city(city_name, country= 'mexico' ):
    """Descirbe a city in a country."""
    print(city_name.title() +  " is a city in " + country.title() + ".")
    
describe_city('tiajuana')
describe_city('cabo')
describe_city('new york', country= 'the u.s')