# Chapter 8

This chapter tells about *Functions*: what is it, how to use it and most importantly how to *call* it.

## Exercise 8-1 Message

```python
def display_message():
    '''Display message'''
    print('This chapter tells about Functions: what is it, how to use it',
    'and most importantly how to call it.')

display_message()
```

**OUTPUT:**

```
This chapter tells about Functions: what is it, how to use it and most importantly how to call it.
```

## Exercise 8-2 Favorite Book

```python
def favourite_book(title):
    '''Display favourite book title'''
    title = str(title)
    print(f'One of my favourite books is {title.title()}.')

favourite_book(1984)
```

**OUTPUT:**

```
One of my favourite books is 1984.
```

## Exercise 8-3 T-Shirt

```python
def make_shirt(size, text):
    '''Display t-shirt size and text on it'''
    print(f'The t-shirt size: {size.upper()}\nPrinted text: {text}\n')

make_shirt('xs', 'i LOVE python')
make_shirt(size='xl', text='god bless python')
```

**OUTPUT:**

```
The t-shirt size: XS
Printed text: i LOVE python

The t-shirt size: XL
Printed text: god bless python

```

## Exercise 8-4 Large Shirts

```python
def make_shirt(size='l', text='i love Python'):
    '''Display t-shirt size and text on it'''
    print(f'The t-shirt size: {size.upper()}\nPrinted text: {text}\n')

make_shirt()
make_shirt(size='m')
make_shirt('s', 'my life is an infinite while and you are a quit')
```

**OUTPUT:**

```
The t-shirt size: L
Printed text: i love Python

The t-shirt size: M
Printed text: i love Python

The t-shirt size: S
Printed text: my life is an infinite while and you are a quit
```

## Exercise 8-5 Cities

```python
def describe_city(city, country='ukraine'):
    '''Display city and its location'''
    print(f'{city.title()} is in {country.capitalize()}')

describe_city('lviv')
describe_city(city='kyiv')
describe_city('belhorod')
```

**OUTPUT:**

```
Lviv is in Ukraine
Kyiv is in Ukraine
Belhorod is in Ukraine
```

## Exercise 8-6 City Names

```python
def city_country(city, country):
    '''Return a city-country pair'''
    pair = f'"{city}, {country}"'
    return pair.title()

pair_1 = city_country('kyiv', 'ukraine')
pair_2 = city_country(city='zagreb', country='croaria')
pair_3 = city_country(country='poland', city='warsaw')

print(f'{pair_1}\n{pair_2}\n{pair_3}')
```

**OUTPUT:**

```
"Kyiv, Ukraine"
"Zagreb, Croaria"
"Warsaw, Poland"
```

## Exercise 8-7 Album

```python
def make_album(artist, album_title, songs_quantity=None):
    """Return a dictionary of information about an album."""
    album = {'artist': artist, 'album_title': album_title}
    if songs_quantity:
        album['songs_quantity'] = songs_quantity
    return album

album_1 = make_album(artist='frank ocean', album_title='blond')
album_2 = make_album(artist='abba', album_title='arrived')
album_3 = make_album(artist='lynyrd skynyrd', album_title='second helping')
print(f'{album_1}\n{album_2}\n{album_3}')

album_4 = make_album(artist='black pumas', album_title='black pumas', 
    songs_quantity='10')
print(f'{album_4}')
```

**OUTPUT:**

```
{'artist': 'frank ocean', 'album_title': 'blond'}
{'artist': 'abba', 'album_title': 'arrived'}
{'artist': 'lynyrd skynyrd', 'album_title': 'second helping'}
{'artist': 'black pumas', 'album_title': 'black pumas', 'songs_quantity': '10'}
```

## Exercise 8-8 User Albums

```python
def make_album(artist, album_title, songs_quantity=None):
    """Return a dictionary of information about an album."""
    album = {'artist': artist, 'album_title': album_title}
    if songs_quantity:
        album['songs_quantity'] = songs_quantity
    return album

while True:
    print('\nTell me your favourire album')
    print('(use "q" any time you want to quit)\n')

    fav_album = input('Tell me your favourite album')
    print(f'inputed value: {fav_album}')
    if fav_album == 'q':
        break
    fav_artist = input('Who made this album?')
    print(f'inputed value: {fav_artist}')
    if fav_artist == 'q':
        break

    album_info = make_album(fav_artist, fav_album)
    print(album_info)
```

**OUTPUT:**

```
Tell me your favourire album
(use "q" any time you want to quit)

inputed value: blond
inputed value: frank ocean
{'artist': 'frank ocean', 'album_title': 'blond'}

Tell me your favourire album
(use "q" any time you want to quit)

inputed value: q
```