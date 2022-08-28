## 1st example 'Changing case in a String', p.20

name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())


## 2nd example 'Using Variables in Strings', p.21

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name)

print(f'Hellp, {full_name.title()}!')

message = f'Hello, {full_name.title()}!'
print(message)

## 3rd example 'Whitespace, Tabs, Newlines', p.22

print('\tPython')

print('languages:\nPyhon\nC\nJavaScript')

print('languages:\n\tPyhon\n\tC\n\tJavaScript')

## 4th example 'Stripping Whitespace'

favourite_language = 'python '
print(favourite_language.rstrip())

favourite_language = favourite_language.rstrip()
print(favourite_language)

favourite_language = ' pyhton '
favourite_language = favourite_language.lstrip()
favourite_language = favourite_language.strip()
print(favourite_language)
