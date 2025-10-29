#This Program will confirm users and their information in a list
# and empty lost to hold confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# verify each user until there are no unconfirmed users
#move each user to confirmed_users after verification
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    

    
# #This Program will store usernames ans their information in a dictionary
# users = {
    
#     'TAhinton': {
#         'first': 'travis',
#         'last': 'hinton',
#         'location': 'new york',
#     },
#     'jdoe': {
#         'first': 'john',
#         'last': 'doe',
#         'location': 'los angeles',
#     },
# }

# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
    
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")