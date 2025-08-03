#This Program will store usernames ans their information in a dictionary
users = {
    
    'TAhinton': {
        'first': 'travis',
        'last': 'hinton',
        'location': 'new york',
    },
    'jdoe': {
        'first': 'john',
        'last': 'doe',
        'location': 'los angeles',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    
