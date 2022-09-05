# Chapter 3

This chapter is *Intoduction to the lists*.

From now on all home tasks will be stored into Python Notebooks, title of which will look like *chapter_**n**_HT*, where **n** is number of the current Chapter.

## Exercise 3-1 Names

```python
names = ['daria', 'dmytro', 'vladyslav', 'krešimir', 'marko']

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])
```

**OUTPUT:**

```
Daria
Dmytro
Vladyslav
Krešimir
Marko
```

## Exercise 3-2 Greetings

```python
names = ['Daria', 'Dmytro', 'Vladyslav', 'Krešimir', 'Marko']

message_0 = f'See ya, {names[-5].title()}!'
message_1 = f'See ya, {names[-4].title()}!'
message_2 = f'See ya, {names[-3].title()}!'
message_3 = f'See ya, {names[-2].title()}!'
message_4 = f'See ya, {names[-1].title()}!'

print(message_0)
print(message_1)
print(message_2)
print(message_3)
print(message_4)
```

**OUTPUT:** 

```
See ya, Daria!
See ya, Dmytro!
See ya, Vladyslav!
See ya, Krešimir!
See ya, Marko!
```

## Exercise 3-3 Your Own List

```python
cars = ['honda', 'audi', 'ford', 'volvo']

print('i want to have ' + cars[0].title() + ' as my first car.')
print(f'i would like to buy {cars[1].title()} in a couple of years.')
print(cars[2].title() + ' has got some pretty nice models.')
print(f'i think {cars[3].title()} is one of the safest cars.')
```

**OUTPUT:**

```
i want to have Honda as my first car.
i would like to buy Audi in a couple of years.
Ford has got some pretty nice models.
i think Volvo is one of the safest cars.
```

## Exercise 3-4 Guest List

```python
guests = ['Nikola Tesla', 'Fritz Perls', 'Grandmother']

message_0 = f'Good Lord, {guests[0]}, you look so thin! Please, attend my dinner on Friday!'
message_1 = f"Hi! Long time no see, {guests[1]}, let's have a chat about unclosed geshtalts of yours!"
message_2 = f'Good to see you again, {guests[2]}! How is your sugar level?'

print(message_0)
print(message_1)
print(message_2)
```

**OUTPUT:**

```
Good Lord, Nikola Tesla, you look so thin! Please, attend my dinner on Friday!
Hi! Long time no see, Fritz Perls, let's have a chat about unclosed geshtalts of yours!
Good to see you again, Grandmother! How is your sugar level?
```

## Exercise 3-5 Changing Guest List

```python
guests = ['Nikola Tesla', 'Fritz Perls', 'Grandmother']
print(f"Unfortunately, {guests[1]} won't make it in time!\n")

guests[1] = 'Sigmund Freid'

message_0 = f'Good Lord, {guests[0]}, you look so thin! Please, attend my dinner on Friday!'
message_1 = f"Hi! How is your childhood traumas, {guests[1]}? Don't tell me, we will have this chat at the dinner!"
message_2 = f'Good to see you again, {guests[2]}! How is your sugar level?'

print(message_0)
print(message_1)
print(message_2)
```

**OUTPUT:**

```
Unfortunately, Fritz Perls won't make it in time!

Good Lord, Nikola Tesla, you look so thin! Please, attend my dinner on Friday!
Hi! How is your childhood traumas, Sigmund Freid? Don't tell me, we will have this chat at the dinner!
Good to see you again, Grandmother! How is your sugar level?
```

# Exercise 3-6 More Guests

```python
guests = ['Nikola Tesla', 'Fritz Perls', 'Grandmother']
print(f"Unfortunately, {guests[1]} won't make it in time!\n")

guests[1] = 'Sigmund Freid'

print('I have just found the bigger table!\n')

guests.insert(0, 'Hieronymus Bosch')
guests.insert(2, 'Nicolas Winding Refn')
guests.append('Martin Luther King Jr.')

message_0 = f'Well, it is not 17th century anymore, {guests[0]}, we have very good food! Come on, dinner will be fine!'
message_1 = f'Good Lord, {guests[1]}, you look so thin! Please, attend my dinner on Friday!'
message_2 = f'Do you have any new idea for you film? Anyway, {guests[2]}, we can talk about it during the dinner!'
message_3 = f"Hi! How is your childhood traumas, {guests[3]}? Don't tell me, we will have this chat at the dinner!"
message_4 = f'Good to see you again, {guests[4]}! How is your sugar level?'
message_5 = f'Jesus Christ, how you even manage your activism in 70s while being a person of color? Very good topic for the dinner you are invited to, {guests[5]}!'

print(message_0)
print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
```

**OUTPUT:**

```
Unfortunately, Fritz Perls won't make it in time!

I have just found the bigger table!

Well, it is not 17th century anymore, Hieronymus Bosch, we have very good food! Come on, dinner will be fine!
Good Lord, Nikola Tesla, you look so thin! Please, attend my dinner on Friday!
Do you have any new idea for you film? Anyway, Nicolas Winding Refn, we can talk about it during the dinner!
Hi! How is your childhood traumas, Sigmund Freid? Don't tell me, we will have this chat at the dinner!
Good to see you again, Grandmother! How is your sugar level?
Jesus Christ, how you even manage your activism in 70s while being a person of color? Very good topic for the dinner you are invited to, Martin Luther King Jr.!
```

## Exercise 3-7 Shriking Guest List

```python
# Exercise 3-7 Shriking Guest List

guests = ['Nikola Tesla', 'Fritz Perls', 'Grandmother']
print(f"Unfortunately, {guests[1]} won't make it in time!\n")

guests[1] = 'Sigmund Freid'

print('I have just found the bigger table!\n')

guests.insert(0, 'Hieronymus Bosch')
guests.insert(2, 'Nicolas Winding Refn')
guests.append('Martin Luther King Jr.')

message_0 = f'Well, it is not 17th century anymore, {guests[0]}, we have very good food! Come on, dinner will be fine!'
message_1 = f'Good Lord, {guests[1]}, you look so thin! Please, attend my dinner on Friday!'
message_2 = f'Do you have any new idea for you film? Anyway, {guests[2]}, we can talk about it during the dinner!'
message_3 = f"Hi! How is your childhood traumas, {guests[3]}? Don't tell me, we will have this chat at the dinner!"
message_4 = f'Good to see you again, {guests[4]}! How is your sugar level?'
message_5 = f'Jesus Christ, how you even manage your activism in 70s while being a person of color? Very good topic for the dinner you are invited to, {guests[5]}!\n'

print(message_0)
print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)

print("Table won't make it in time, so i can invite only two people. Please, accept my sincere appologies!\n")

non_guest_1 = guests.pop(0)
non_guest_2 = guests.pop(0)
non_guest_3 = guests.pop(1)
non_guest_4 = guests.pop(1)

print(f'{non_guest_1} was removed from the list...\n')
print(non_guest_2 + ' was banned from the community...\n')
print(f'{non_guest_3} are dead...\n')
print(non_guest_4 + ' is a bad person...\n')

print(f'You are still invited, {guests[0]}')
print(guests[1] + ' see you ar the dinner, mate!\n')

del guests[0]
del guests[0]

print(guests)
```

**OUTPUT:**

```
Table won't make it in time, so i can invite only two people. Please, accept my sincere appologies!

Hieronymus Bosch was removed from the list...

Nikola Tesla was banned from the community...

Sigmund Freid are dead...

Grandmother is a bad person...

You are still invited, Nicolas Winding Refn
Martin Luther King Jr. see you ar the dinner, mate!

[]
```

## Exercise 3-8 Seeing the World

```python
locations = ['Florence', 'The Faroe Islands', 'New York', 'Barcelona', 'The Grand Canyon', 'Norway', 'Amsterdam', 'Phuket']
print(locations)

print(sorted(locations)) # sorting temporarily
print(f'\nOriginal list: {locations}\n')

print(sorted(locations, reverse=True)) # sorting in reverse tem
print(f'\nOriginal list again: {locations}\n')

locations.reverse() # permanent reverse
print(locations)

locations.reverse() # permanent reverse of reverse
print(locations)

locations.sort() # permanent sorting
print(locations)

locations.sort(reverse=True) # permanent reversed sorting
print(locations)
```

**OUTPUT:**

```
['Florence', 'The Faroe Islands', 'New York', 'Barcelona', 'The Grand Canyon', 'Norway', 'Amsterdam', 'Phuket']
['Amsterdam', 'Barcelona', 'Florence', 'New York', 'Norway', 'Phuket', 'The Faroe Islands', 'The Grand Canyon']

Original list: ['Florence', 'The Faroe Islands', 'New York', 'Barcelona', 'The Grand Canyon', 'Norway', 'Amsterdam', 'Phuket']

['The Grand Canyon', 'The Faroe Islands', 'Phuket', 'Norway', 'New York', 'Florence', 'Barcelona', 'Amsterdam']

Original list again: ['Florence', 'The Faroe Islands', 'New York', 'Barcelona', 'The Grand Canyon', 'Norway', 'Amsterdam', 'Phuket']

['Phuket', 'Amsterdam', 'Norway', 'The Grand Canyon', 'Barcelona', 'New York', 'The Faroe Islands', 'Florence']
['Florence', 'The Faroe Islands', 'New York', 'Barcelona', 'The Grand Canyon', 'Norway', 'Amsterdam', 'Phuket']
['Amsterdam', 'Barcelona', 'Florence', 'New York', 'Norway', 'Phuket', 'The Faroe Islands', 'The Grand Canyon']
['The Grand Canyon', 'The Faroe Islands', 'Phuket', 'Norway', 'New York', 'Florence', 'Barcelona', 'Amsterdam']
```

## Exercise 3-9 Dinner Guests

```python
guests = ['Nikola Tesla', 'Fritz Perls', 'Grandmother']

message_0 = f'Good Lord, {guests[0]}, you look so thin! Please, attend my dinner on Friday!'
message_1 = f"Hi! Long time no see, {guests[1]}, let's have a chat about unclosed geshtalts of yours!"
message_2 = f'Good to see you again, {guests[2]}! How is your sugar level?'

print(message_0)
print(message_1)
print(message_2)

print(f'\nTo the dinner were invited {len(guests)} people.')
```

**OUTPUT:**

```
Good Lord, Nikola Tesla, you look so thin! Please, attend my dinner on Friday!
Hi! Long time no see, Fritz Perls, let's have a chat about unclosed geshtalts of yours!
Good to see you again, Grandmother! How is your sugar level?

To the dinner were invited 3 people.
```

## Exercise 3-10 Every Function

```python
jewelry = ['ring', 'bracelet', 'earings']
accessories = ['watch', 'glasses', 'parfume']
tech = ['laptop', 'earpods']

belongins = jewelry + accessories + tech #c reate a full list
print(belongins)

belongins.append('phone') # add a new element to the list
print(belongins)

belongins.insert(2, 'necklace') # add one more element
print(belongins)

del belongins[6] # permanent deleting of an element
print(belongins)

lost_item = belongins.pop(-2) # popping an element and storing it into variable
print(f'\ni have lost my {lost_item.title()}')
print(belongins)

broken_item = 'bracelet'
belongins.remove(broken_item) # remove via value
print(f'\nunfortunately, i accidentally broke my {broken_item}')
print(belongins)

print(sorted(belongins)) # temporary sorting
print(sorted(belongins, reverse=True)) # temporary reversed sorting

belongins.reverse() # permanent reversing of the list
print(belongins)

belongins.sort(reverse=True) # permanent reversed sorting of the list in alphabetic order
print(belongins)

items_amount = len(belongins) # list lenght
print('\ni have at least ' + str(items_amount) + ' items with myself.')
```
**OUTPUT:**

```
['ring', 'bracelet', 'earings', 'watch', 'glasses', 'parfume', 'laptop', 'earpods']
['ring', 'bracelet', 'earings', 'watch', 'glasses', 'parfume', 'laptop', 'earpods', 'phone']
['ring', 'bracelet', 'necklace', 'earings', 'watch', 'glasses', 'parfume', 'laptop', 'earpods', 'phone']
['ring', 'bracelet', 'necklace', 'earings', 'watch', 'glasses', 'laptop', 'earpods', 'phone']

i have lost my Earpods
['ring', 'bracelet', 'necklace', 'earings', 'watch', 'glasses', 'laptop', 'phone']

unfortunately, i accidentally broke my bracelet
['ring', 'necklace', 'earings', 'watch', 'glasses', 'laptop', 'phone']
['earings', 'glasses', 'laptop', 'necklace', 'phone', 'ring', 'watch']
['watch', 'ring', 'phone', 'necklace', 'laptop', 'glasses', 'earings']
['phone', 'laptop', 'glasses', 'watch', 'earings', 'necklace', 'ring']
['watch', 'ring', 'phone', 'necklace', 'laptop', 'glasses', 'earings']

i have at least 7 items with myself.
```

## Exercise 3-11 Intentional Error

```python
jewelry = ['ring', 'bracelet', 'earings'] # create a full list
del jewelry[3]
```

**OUTPUT:**

```python
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
/Users/olhababenko/Documents/projects/crash_course/chapter_3/chapter_3_HT.ipynb Cell 11 in <cell line: 4>()
      1 # Exercise 3-11 Intentional Error
      3 jewelry = ['ring', 'bracelet', 'earings'] # create a full list
----> 4 del jewelry[3]

IndexError: list assignment index out of range
```