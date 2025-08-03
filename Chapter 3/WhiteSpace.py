# This program demonstrates the use of whitespace in Python strings.
favorite_language = ' Python '
favorite_language = favorite_language.strip()
favorite_language = favorite_language.strip()
print(favorite_language)

nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)