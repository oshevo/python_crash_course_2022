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