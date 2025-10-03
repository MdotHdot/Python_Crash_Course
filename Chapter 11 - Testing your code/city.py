#user inpute program for cityies and countries
from city_country_function import get_city_country
print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me a city: ")
    if city == 'q':
        break
    country = input("Please give me a country: ")
    if country == 'q':
        break
    formatted_country = get_city_country(city, country)
    print(f"\tNeatly formatted description: {formatted_country}.")