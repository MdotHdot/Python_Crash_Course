# returning a dictionary
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {
        'first': first_name,
        'last': last_name
    }
    if age:
        person['age'] = age
    return person
# This will use the function to build a person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)  # Output: {'first': 'jimi', 'last': 'hendrix'}
musician = build_person('curtis', 'jackson')
print(musician)  # Output: {'first': 'curtis', 'last': 'jackson'}
    