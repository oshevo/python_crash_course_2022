# Chapter 6

In this chapter we will find out about *Dictionaries*, how to create and operate them.

## Exercise 6-1 Person

```python
person = {
    'name': 'dasha',
    'surname': 'reheta',
    'age': 24,
    'city': 'Kyiv'
    }

print(person['name'].title())
print(person['surname'].title())
print(person['age'])
print(person['city'].title())
```

**OUTPUT:**

```
Dasha
Reheta
24
Kyiv
```

## Exercise 6-2 Favourite Numbers

```python
favourite_numbers = {
    'dasha': 62,
    'natasha': 8,
    'ivan': 69,
    'dima': 124,
    'marko': 1}

for name, number in favourite_numbers.items():
    print(f'{name.capitalize()}`s favourite number is {number}')
```

**OUTPUT:**

```
Dasha`s favourite number is 62
Natasha`s favourite number is 8
Ivan`s favourite number is 69
Dima`s favourite number is 124
Marko`s favourite number is 1
```

## Exercise 6-3 Glossary

```python
glossary = {
    'dictionary': 'is a collection of key-value pairs',
    'tuple': 'is an immutable list',
    'traceback': 'is an error report',
    'directory': 'is a collection of files and subdirectories',
    'value': 'is the information associated with that variable',
    }

for word, definition in glossary.items():
    print(f'| A {word} | \n\t{definition}')
```

**OUTPUT:**

```
| A dictionary | 
	is a collection of key-value pairs
| A tuple | 
	is an immutable list
| A traceback | 
	is an error report
| A directory | 
	is a collection of files and subdirectories
| A value | 
	is the information associated with that variable
```

## Exercise 6-4 Glossary 2

```python
glossary = {
    'dictionary': 'is a collection of key-value pairs',
    'tuple': 'is an immutable list',
    'traceback': 'is an error report',
    'directory': 'is a collection of files and subdirectories',
    'value': 'is the information associated with that variable',
    }

glossary['string'] = 'is a series of characters'
glossary['method'] = 'is an action that Python can perform on a piece of data'
glossary['whitespace'] = 'is any nonprinting character, such as spaces, tabs, etc.'
glossary['index'] = 'is the position of the element into list'
glossary['list comprehension'] = 'is a way to generate a list in one line of code'
    

for word, definition in glossary.items():
    print(f'| A {word} | \n\t{definition}')
```

**OUTPUT:**

```| A dictionary | 
	is a collection of key-value pairs
| A tuple | 
	is an immutable list
| A traceback | 
	is an error report
| A directory | 
	is a collection of files and subdirectories
| A value | 
	is the information associated with that variable
| A string | 
	is a series of characters
| A method | 
	is an action that Python can perform on a piece of data
| A whitespace | 
	is any nonprinting character, such as spaces, tabs, etc.
| A index | 
	is the position of the element into list
| A list comprehension | 
	is a way to generate a list in one line of code
```

## Exercise 6-5 Rivers

```python
rivers = {
    'ukraine': 'dnipro',
    'egypt': 'nile',
    'brazil': 'amazon'
    }

for country, river in rivers.items():
    print(f'{river.capitalize()} runs through {country.capitalize()}.')

for river in rivers.values():
    print(river.capitalize())

for country in rivers.keys():
    print(country.capitalize())
```

**OUTPUT:**

```
Dnipro runs through Ukraine.
Nile runs through Egypt.
Amazon runs through Brazil.
Dnipro
Nile
Amazon
Ukraine
Egypt
Brazil
```

## Exercise 6-6 Polling

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

respondents = ['Sarah', 'paul', 'Richard', 'chadwick', 'Edward']

for respondent in respondents:
    if respondent.lower() in favorite_languages.keys():
        print(f'{respondent.capitalize()}, thank you for the answer!')
    else:
        print(f'{respondent.capitalize()}, please take our poll!')
```

**OUTPUT:**

```
Sarah, thank you for the answer!
Paul, please take our poll!
Richard, please take our poll!
Chadwick, please take our poll!
Edward, thank you for the answer!
```

## Exercise 6-7 People


```python
person_1 = {
    'name': 'dasha',
    'surname': 'reheta',
    'age': 24,
    'city': 'Kyiv'
    }

person_2 = {
    'name': 'yaroslav',
    'surname': 'voloschuk',
    'age': 32,
    'city': 'lviv'
    }

person_3 = {
    'name': 'marko',
    'surname': 'kovačević',
    'age': 26,
    'city': 'zagreb'
    }

people = [person_1, person_2, person_3]

for person in people:
    print(person)
```

**OUTPUT:**

```{'name': 'dasha', 'surname': 'reheta', 'age': 24, 'city': 'Kyiv'}
{'name': 'yaroslav', 'surname': 'voloschuk', 'age': 32, 'city': 'lviv'}
{'name': 'marko', 'surname': 'kovačević', 'age': 26, 'city': 'zagreb'}
```

## Exercise 6-8 Pets

```python
pet_1 = {
    'kind': 'cat',
    'owner': 'dasha'
    }

pet_2 = {
    'kind': 'dog',
    'owner': 'marko'
    }

pet_3 = {
    'kind': 'rabbit',
    'owner': 'ivan'
    }

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(pet)
```

**OUTPUT:**

```
{'kind': 'cat', 'owner': 'dasha'}
{'kind': 'dog', 'owner': 'marko'}
{'kind': 'rabbit', 'owner': 'ivan'}
```

## Exercise 6-9 Favorite Places

```python
favourite_places = {
    'dasha': ['kyiv', 'berdychiv'],
    'ivan': ['chernivtsi', 'lviv'],
    'natasha': ['zagreb', ]
    }

for name, locations in favourite_places.items():
    if len(locations) > 1:
        print(f'{name.capitalize()}`s favourite locations are:')
    else:
        print(f'{name.capitalize()}`s favourite location is:')
    for location in locations:
        print(f'\t{location.capitalize()}')
```

**OUTPUT:**

```
Dasha`s favourite locations are:
	Kyiv
	Berdychiv
Ivan`s favourite locations are:
	Chernivtsi
	Lviv
Natasha`s favourite location is:
	Zagreb
```

## Exercise 6-10 Favourite Numbers

```python
favourite_numbers = {
    'dasha': [],
    'natasha': [8, 4367, 37, 21,],
    'ivan': [69, 1,],
    'dima': [124, 54],
    'marko': [1,]}

for name, numbers in favourite_numbers.items():
    if len(numbers) < 1:
        print(f'{name.capitalize()} does not have a favourite number.')
    elif len(numbers) > 1:
        print(f'{name.capitalize()}`s favourite numbers are:')
    else:
        print(f'{name.capitalize()}`s favourite number is')
    for number in numbers:
        print(f'{number}')
```

**OUTPUT:**
```
Dasha does not have a favourite number.
Natasha`s favourite numbers are:
8
4367
37
21
Ivan`s favourite numbers are:
69
1
Dima`s favourite numbers are:
124
54
Marko`s favourite number is
1
```

## Exercise 6-11 Cities

```python
cities = {
    'kyiv': {
        'country': 'ukraine',
        'population': 2.96,
        'area': 839,
        'fact': 'was founded in 482 AD',
        },
    'zagreb': {
        'country': 'croatia',
        'population': 0.77,
        'area': 641,
        'fact': 'has the shortest time for a public' 
            'transport vehicle in the world',
        },
    'edinburgh': {
        'country': 'scotland',
        'population': 0.51,
        'area': 264,
        'fact': 'is the greenest city in the UK',
        }
    }

for city, city_info in cities.items():
    print(f'\tCity:\n\t{city.capitalize()}')
    country = city_info['country']
    population = city_info['population']
    area = city_info['area']
    fact = city_info['fact']

    print(f'{city.capitalize()} is located in {country.capitalize()}. '
        f'Population of the city is {population} millions people, '
        f'while area is {area} km\u00B2. {city.capitalize()} {fact}.')
```

**OUTPUT:**
```
    City:
	Kyiv
Kyiv is located in Ukraine. Population of the city is 2.96 millions people, while area is 839 km². Kyiv was founded in 482 AD.
	City:
	Zagreb
Zagreb is located in Croatia. Population of the city is 0.77 millions people, while area is 641 km². Zagreb has the shortest time for a publictransport vehicle in the world.
	City:
	Edinburgh
Edinburgh is located in Scotland. Population of the city is 0.51 millions people, while area is 264 km². Edinburgh is the greenest city in the UK.
```

## Exercise 6-12 Extensions

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}

user = 'sfreud'

if user not in users.keys():
    print(f'user "{user}" is not found. please, register first!')
else:
    for username, user_info in users.items():
        if username == user:
            print(f"\nUsername: {username}")
            full_name = f"{user_info['first']} {user_info['last']}"
            location = user_info['location']
        
            print(f"\tFull name: {full_name.title()}")
            print(f"\tLocation: {location.title()}")

users['sfreud'] = {'first': 'sigmund', 
                    'last': 'freud', 
                    'location': 'freiberg'
                    }

new_user = 'sfreud'

if new_user not in users.keys():
    print(f'user "{new_user}" is not found. please, register first!')
else:
    print(f'\nthank you for the registration, {new_user}!')
    for username, user_info in users.items():
        if username == new_user:
            full_name = f"{user_info['first']} {user_info['last']}"
            location = user_info['location']
        
            print(f"\tFull name: {full_name.title()}")
            print(f"\tLocation: {location.title()}")
```

**OUTPUT**
```
user "sfreud" is not found. please, register first!

thank you for the registration, sfreud!
	Full name: Sigmund Freud
	Location: Freiberg
```