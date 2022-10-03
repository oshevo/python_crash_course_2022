# Chapter 7

In this chapter we will learn about *input()*, *while looping* and how to use them with lists and dictionaries.

## Exercise 7-1 Rental Car

```python
car = input('Which car would you like to get?')
print(f'inputed value: {car}')

print(f'\nHmmmm...Hold on, please, I`ll check if we have {car.capitalize()}.')
```

**OUTPUT:**

```
inputed value: audi

Hmmmm...Hold on, please, I`ll check if we have Audi.
```

## Exercise 7-2 Restaurant Seating

```python
guests_quantity = int(input('How many people are in your dinner group?'))
print(f'inputed value: {guests_quantity}')

if guests_quantity > 8:
    print(f'\nPlease, wait for a free table.')
else:
    print(f'\nYour table is ready!')
```

**OUTPUT:**
```
inputed value: 8

Your table is ready!
```

## Exercise 7-4 Pizza Toppings

```python
prompt = '\nPlease, enter the toppings you want to add to your pizza.'
prompt += '\nP.S.: Enter "quit" if you are finished.'

topping = ''

while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f'{topping.capitalize()} is added!')
```

**OUTPUT:**

```
Mozarella is added!
Feferoni is added!
```

## Exercise 7-5 Movie Tickets

```python
prompt = '\nPlease, enter your age:'
prompt += '\nP.S.: Enter "quit" if you are finished.'

active = True
while active:
    age = input(prompt)
    
    if age != 'quit':
        print(f'inputed value: {age} y.o.')

    if age == 'quit':
        active = False
    elif int(age) < 3:
        print(f'For the person under age of 3 y.o. ticket is free.\n')
    elif 3 < int(age) <= 12:
        print(f'For person between 3 and 12 y.o. ticket costs 10$.\n')
    else:
        print(f'For person over 12 y.o. ticket costs 15$.\n')
```

**OUTPUT:**

```
inputed value: 1 y.o.
For the person under age of 3 y.o. ticket is free.

inputed value: 6 y.o.
For person between 3 and 12 y.o. ticket costs 10$.

inputed value: 67 y.o.
For person over 12 y.o. ticket costs 15$.
```

## Exercise 7-6 Three Exits

```python
prompt = '\nPlease, enter the toppings you want to add to your pizza.'
prompt += '\nP.S.: Enter "quit" if you are finished.'

# Active variable
active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f'{topping.capitalize()} is added!')

# Break statement
while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f'{topping.capitalize()} is added!')
```

**OUTPUT:**

```
Feferoni is added!
Mozarella is added!
Pineapples is added!
Nutella is added!
```

## Exercise 7-7 Infinity

```python
a = 0
while a <= 10:
    print(f'{a}')
```

**OUTPUT:**

```
Output exceeds the size limit. Open the full output data in a text editor
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
...
0
0
0
0
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
/Users/olhababenko/Documents/projects/crash_course/chapter_7/chapter_7_HT.ipynb Cell 7 in <cell line: 2>()
      1 a = 0
      2 while a <= 10:
----> 3     print(f'{a}')

KeyboardInterrupt:
```

## Exercise 7-8 Deli

```python
sandwich_orders = ['chicken', 'egg', 'salmon', 'tuna', 'roast beef', ]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f'I made your {current_sandwich} sandwitch!')
    finished_sandwiches.append(current_sandwich)

print(f'\n---- Prepared orders ----')
for sandwich in finished_sandwiches:
    print(sandwich)
```

**OUTPUT:**

```
I made your roast beef sandwitch!
I made your tuna sandwitch!
I made your salmon sandwitch!
I made your egg sandwitch!
I made your chicken sandwitch!

---- Prepared orders ----
roast beef
tuna
salmon
egg
chicken
```

## Exercise 7-9 No Pastrami

```python
sandwich_orders = ['chicken', 'pastrami', 'egg', 'salmon', 'pastrami', 'tuna',
                 'roast beef', 'pastrami',]
finished_sandwiches = []

print(f'Unfortunately, Deli has run out of pastrami :(\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f'I made your {current_sandwich} sandwitch!')
    finished_sandwiches.append(current_sandwich)

print(f'\n---- Prepared orders ----')
for sandwich in finished_sandwiches:
    print(sandwich)
```

**OUTPUT:**

```
Unfortunately, Deli has run out of pastrami :(

I made your roast beef sandwitch!
I made your tuna sandwitch!
I made your salmon sandwitch!
I made your egg sandwitch!
I made your chicken sandwitch!

---- Prepared orders ----
roast beef
tuna
salmon
egg
chicken
```

## Exercise 7-10 Dream Vacation

```python
places = {}

polling_active = True
while polling_active:
    username = input('\nEnter your username, please:')
    place = input('\nWhen Ukraine wins the war, where will you go?')

    places[username] = place

    repeat = input('Would you like to let another person respond? (y/ n)')
    if repeat == 'n' or repeat == 'no':
        polling_active = False

print(f'---- Results ----')
for username, place in places.items():
    print(f'{username} will go to {place.capitalize()}')
```

**OUTPUT:**

```
---- Results ----
oshevo will go to Crimea
vangalavan will go to Donetsk
```