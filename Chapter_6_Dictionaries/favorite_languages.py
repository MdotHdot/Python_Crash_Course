#This program see what are users favorite languages

favorite_languages = { 
    'jen': ['python', 'javascript'], # key is the name of the user and value is a list of languages
    'sarah': ['c', 'python'],
    'edward': ['ruby', 'c'],
     'phil': ['python'],
    'sam': ['java', 'c++'],
    'alfie': ['c++', 'java', 'python'],
    'tasha': ['ruby'],
}
for name, languages in favorite_languages.items():
    if len(languages) > 1:# iterating through the dictionary
        print(f" {name.title()}'s favorite Language is:") # printing the key and value of the dictionary
        for language in languages: # iterating through the value of the dictionary
            print(f"\t{language.title()}")
   

# friends = ['sarah', 'edward']
# not_polled = ['jeff', 'erin'] # list of users who have not taken the poll
# for name, language in favorite_languages.items(): # iterating through the dictionary
#     print(f" Hi {name.title()}!") # printing the key and value of the dictionary
    
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"I see you like to use  {language}.")
    
# if name not in favorite_languages and name in not_polled:  # checking if the name is not in the dictionary but is in the not_polled list
#     print(f"{name.title()}, please take our poll!")
    
# for name in sorted(favorite_languages.keys()): # iterating through the dictionary
#     print(f"{name.title()}, thank you for taking the poll!") # printing the key of the dictionary

# print(f"\nThe following languages have been mentioned:") 
# for lanuage in set(favorite_languages.values()):
#     print(lanuage.title())

#     print(language.title())
# language = favorite_languages['edward'].title() # getting the value of the key 'sarah' in the dictionary and converting it to title case
# print(f"Sarah's favorite language is {language}.") # printing the value of the key 'sarah' in the dictionary