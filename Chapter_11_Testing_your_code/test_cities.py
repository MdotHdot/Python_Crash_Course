#testing city and country functions
import pytest
from city_country_function import get_city_country
def test_city_country():
    '''Do names like 'Santiago, Chile' work?'''
    formatted_country = get_city_country('santiago', 'chile')
    assert formatted_country == 'Santiago Chile '
    
def test_city_country_population():
    '''Do names like 'Santiago, Chile - population 5000000' work?'''
    formatted_country = get_city_country('santiago', 'chile', '5000000')
    assert formatted_country == 'Santiago  Chile - Population 5000000 '