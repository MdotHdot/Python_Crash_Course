rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'mississippi': 'usa',
    'thames': 'uk',
    'ganges': 'india',
    'danube': 'austria',
    'volga': 'russia',
    'seine': 'france',
    'tigris': 'iraq',
    'arun': 'uk',
    
    
    
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe following rivers are in the dictionary:")
for river in sorted(rivers.keys()):
    print(river.title()) #this will print all rivers in a sorted order
print("\nThis is the list of countrys with famous rivers:")   
for country in sorted(set(rivers.values())):
    print(country.title()) #this will sort  all countires in a set order so there are no duplicates. 