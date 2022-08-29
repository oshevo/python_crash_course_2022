# Chapter 2

This chapter is a briefly introduction to *Variables and Simple Data Types*.

## Exercise 2-1 Simple Message

It can be found into file **simple_message.py**, which is located into root of folder *chapter_2*.

```sh
my_age = 24
print(my_age)

OUTPUT:
24
```

## Exercise 2-2 Simple Messages

It can be found into file **simple_messages.py**, which is located into root of folder *chapter_2*.

```sh
my_day = 'awful'
print(my_day)

my_day = 'bearable'
print(my_day)

OUTPUT:
awful
bearable
```

## Exercise 2-3 Personal Message

It can be found into file **personal_message.py**, which is located into root of folder *chapter_2*.

```sh
name = 'olha babenko'

print(f'Hello {name}, how is Python learning going?')

OUTPUT:
Hello olha babenko, how is Python learning going?
```

## Exercise 2-4 Name Cases

It can be found into file **name_cases.py**, which is located into root of folder *chapter_2*.

```sh
name = 'olha babenko'

print(name.title()) 
print(name.upper())
print(name.lower())

OUTPUT:
Olha Babenko
OLHA BABENKO
olha babenko
```

## Exercise 2-5 Famous Quote

It can be found into file **famous_quote.py**, which is located into root of folder *chapter_2*.

- 1st way
```sh
print('Epicurus once said, "When we are, death is not come, and, when death is come, we are not."')

OUTPUT:
Epicurus once said, "When we are, death is not come, and, when death is come, we are not."
```

- 2nd way

```sh
quote = 'When we are, death is not come, and, when death is come, we are not.'
author = 'Epicurus'

print(f'{author} once said, "{quote}"')

OUTPUT:
Epicurus once said, "When we are, death is not come, and, when death is come, we are not."
```

- 3rd way

```sh
quotation = f'{author} once said, "{quote}"'

print(quotation)

OUTPUT:
Epicurus once said, "When we are, death is not come, and, when death is come, we are not."
```

## Exercise 2-6 Famous Quote 2

It can be found into file **famous_quote_2.py**, which is located into root of folder *chapter_2*.

```sh
famous_person = 'Epicurus'
message = f'{famous_person} once said, "When we are, death is not come, and, when death is come, we are not."'

print(message)

OUTPUT:
Epicurus once said, "When we are, death is not come, and, when death is come, we are not."
```

## Exercise 2-7 Stripping Names

It can be found into file **stripping_name.py**, which is located into root of folder *chapter_2*.

```sh
name = ' \tOlha babenko\n '

print(name)

print(name.lstrip())
print(name.rstrip())
print(name.strip())

OUTPUT:
 	Olha babenko
 
Olha babenko
 
 	Olha babenko
Olha babenko
```

## Exercise 2-8 Number Eight

It can be found into file **number_eight.py**, which is located into root of folder *chapter_2*.

```sh
print(4 + 4)
print(98 - 90)
print(0.125 * 64)
print(72 / 9)

OUTPUT:
8
8
8.0
8.0
```

## Exercise 2-9 Favourite Number

It can be found into file **favourite_number.py**, which is located into root of folder *chapter_2*.

```sh
favourite_number = 5.6
message = f'My favourite number is {favourite_number}.'

print(message)

OUTPUT:
My favourite number is 5.6.
```

## Exercise 2-10 Adding Comments

Comments were added into 2 files, which are located into root of folder *chapter_2*:

1. name_cases.py

```sh
name = 'olha babenko' # both announcing variable and giving the value to it

print(name.title()) # title method, word begins with upper case
print(name.upper()) # upper method, whole word is in upper case
print(name.lower()) # lower method, whole word is in lower case
```

2. stripping_name.py

```sh
# program will strip the whitespaces from the string variable

name = ' \tOlha babenko\n ' # announcing variable, adding value with neccesary requirements

print(name) # printing the result

print(name.lstrip()) # printing with deleting whitespaces on the left part
print(name.rstrip()) # printing with deleting whitespaces on the right part
print(name.strip()) # printing with deleting whitespaces from all the word
```

## Exercise 2-11 Zen of Python

> The Zen of Python, by Tim Peters

> Beautiful is better than ugly.
> Explicit is better than implicit.
> Simple is better than complex.
> Complex is better than complicated.
> Flat is better than nested.
> Sparse is better than dense.
> Readability counts.
> Special cases aren't special enough to break the rules.
> Although practicality beats purity.
> Errors should never pass silently.
> Unless explicitly silenced.
> In the face of ambiguity, refuse the temptation to guess.
> There should be one-- and preferably only one --obvious way to do it.
> Although that way may not be obvious at first unless you're Dutch.
> Now is better than never.
> Although never is often better than *right* now.
> If the implementation is hard to explain, it's a bad idea.
> If the implementation is easy to explain, it may be a good idea.
> Namespaces are one honking great idea -- let's do more of those!

***THE END of the 2nd Chapter***