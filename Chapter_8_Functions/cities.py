def city_country(city, country='USA'):
    """Display information about a city and its country."""
    print(f"{city.title()} is in {country.title()}.")
# calling the function with positional arguments
city_country('new york')  # calling the function with default country
city_country('los angeles')  # calling the function with default country
city_country('tokyo', country='japan')  # calling the function with a different country
    
    
    








#Describe Cities using Fuctions
# def describe_city(city, country='USA'):
#     """Display information about a city."""
#     print(f"\n{city} is in {country}.")
    
# describe_city('New York')  # calling the function with default country
# describe_city('Los Angeles')  # calling the function with default country
# describe_city( 'Japan', country='Tokyo')  # calling the function with a different 
