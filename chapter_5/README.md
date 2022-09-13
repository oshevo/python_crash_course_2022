# Chapter 5

In this chapter we will take a look on the *IF Statements* and how to use them.

## Exercise 5-1, 5-2 Cinditional Tests, More Conditional Tests

```python
my_pizza = 'peperoni'
friend_pizza = 'Vesuvio'

print('Is peperoni my favourite pizza?')
print(my_pizza.lower() == 'peperoni')

print("Is peperoni my friend's favourite pizza?")
print(friend_pizza.lower() == 'vesuvio')

print("\nWe don't like the same pizza, do we?")
print(friend_pizza.lower() != friend_pizza)

print('Is capriciosa my favourite pizza?')
print(my_pizza.lower() == 'capriciosa')

my_number = 37
friend_number = 5

print('\nIs my number more than 23?')
print(my_number > 23)

print('Is my number bigger than my friend`s?')
print(my_number < friend_number)

print('Is my number equal to 71?')
print(my_number == 71)

print('\nIs my number between 30 and 50?')
print(my_number <= 30 and my_number >= 50)

print('Is my friend`s number more than 10 or more than 20?')
print(friend_number > 10 or friend_number > 20)

print('Is my friend`s number not equal to mine?')
print(my_number != friend_number)

numbers = [value*2 for value in range(1, 8, 2)]
print('\nIs number 14 in the list?')
print(14 in numbers)

print('Is number 8 in the list?')
print(8 in numbers)
```
**OUTPUT:**

```
Is peperoni my favourite pizza?
True
Is peperoni my friend's favourite pizza?
True

We don't like the same pizza, do we?
True
Is capriciosa my favourite pizza?
False

Is my number more than 23?
True
Is my number bigger than my friend`s?
False
Is my number equal to 71?
False

Is my number between 30 and 50?
False
Is my friend`s number more than 10 or more than 20?
False
Is my friend`s number not equal to mine?
True

Is number 14 in the list?
True
Is number 8 in the list?
False
```

## Exercise 5-3 Alien Colors #1

```python
alien_color = 'yellow'

if alien_color == 'yellow':
    print ('You have earned 5 points!')

if alien_color == 'green':
    print ('You have earned 15 points!')
```

**OUTPUT:**

```
You have earned 5 points!
```

## Exercise 5-4 Alien Colors #2

```python
alien_color = 'green'

## 1st version
if alien_color == 'green':
    print('You have earned 5 points!')
if alien_color != 'green':
    print('You have earned 10 points!')

## 2nd version
if alien_color == 'green':
    print('You have earned 5 points!')
else:
    print('You have earned 10 points!')
```

**OUTPUT:**
```
You have earned 5 points!
You have earned 5 points!
```

## Exercise 5-5 Alien Colors #3

```python
## 1st version
alien_color = 'green'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print(f'You have earned {points} points!')


## 2nd version
alien_color = 'yellow'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print(f'You have earned {points} points!')


## 3rd version
alien_color = 'red'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print(f'You have earned {points} points!')
```

**OUTPUT:**
```
You have earned 5 points!
You have earned 10 points!
You have earned 15 points!
```

## Esercise 5-6 Stages of Life

```python
age = 24

if age < 2:
    stage = 'a baby'
elif 2 <= age < 4:
    stage = 'a toddler'
elif 4 <= age < 13:
    stage = 'a kid'
elif 13 <= age < 20:
    stage = 'a teenager'
elif 20 <= age < 65:
    stage = 'an adult'
else:
    stage = 'an elder'

print(f'You are {stage}.')
```

**OUTPUT:**

```
You are an adult.
```

## Exercise 5-7 Favorite Fruit

```python
favourite_fruit = ['mango', 'strawberry', 'blueberry']

if 'mango' in favourite_fruit:
    print(f'Jesus Christ, your favourite fruit is mango!')
if 'banana' in favourite_fruit:
    print(f'Are you insane? I bet you do, cause your favourite fruit is banana')
if 'raspberry' in favourite_fruit:
    print(f'You can`t be serious! Is raspberry your favourite fruit?')
if 'apple' in favourite_fruit:
    print(f'I`ll never talk to you again, cause your favourite fruit is apple!')
if 'strawberry' in favourite_fruit:
    print(f'OMG, unbelievable! Who on Earth like strawberry?')
```

**OUTPUT:**

```
Jesus Christ, your favourite fruit is mango!
OMG, unbelievable! Who on Earth like strawberry?
```

## Exercise 5-8 Hello Admin

```python
usernames = ['admin', 'olha', 'nataliia', 'ivan', 'anna', 'oksana', 'roman']

for username in usernames:
    if username == 'admin':
        print(f'Hello {username}, would you like to see a status report?')
    else:
        print(f'Hello {username.capitalize()}, thank you for logging in!')
```

**OUTPUT:**

```
Hello admin, would you like to see a status report?
Hello Olha, thank you for logging in!
Hello Nataliia, thank you for logging in!
Hello Ivan, thank you for logging in!
Hello Anna, thank you for logging in!
Hello Oksana, thank you for logging in!
Hello Roman, thank you for logging in!
```

## Exercise 5-9 No Users

```python
# usernames = ['admin', 'olha', 'nataliia', 'ivan', 'anna', 'oksana', 'roman']
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username}, would you like to see a status report?')
        else:
            print(f'Hello {username.capitalize()}, thank you for logging in!')
else:
    print('We need to find some users!') 
```

**OUTPUT:**

```
We need to find some users!
```

## Exercise 5-10 hecking Usernames


```python
current_users = ['Angel', 'the_pooh', 'lollipop69', 'your_crush',
                 'devil_himself', 'Beauty', 'badass']

current_users = [current_user.lower() for current_user in current_users]

new_users = ['demon', 'albert', 'beauty', 'beast', 'BADASS']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'"{new_user}" is unavailable. Please, create new username.')
    else:
        print(f'"{new_user}" is available!')
```

**OUTPUT:**

```
"demon" is available!
"albert" is available!
"beauty" is unavailable. Please, create new username.
"beast" is available!
"BADASS" is unavailable. Please, create new username.
```

## Exercise 5-11 Ordinal Numbers

```python
ordinary_numbers = list(range(1,10))

for ordinary_number in ordinary_numbers:
    if ordinary_number == 1:
        print(f'{ordinary_number}st')
    elif ordinary_number == 2:
        print(f'{ordinary_number}nd')
    elif ordinary_number == 3:
        print(f'{ordinary_number}rd')
    else:
        print(f'{ordinary_number}th')
```

**OUTPUT:**
```
1st
2nd
3rd
4th
5th
6th
7th
8th
9th
```
