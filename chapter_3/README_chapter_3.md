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

OUTPUT:
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

OUTPUT:
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

OUTPUT:
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

OUTPUT:
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

OUTPUT:
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

OUTPUT:

Unfortunately, Fritz Perls won't make it in time!

I have just found the bigger table!

Well, it is not 17th century anymore, Hieronymus Bosch, we have very good food! Come on, dinner will be fine!
Good Lord, Nikola Tesla, you look so thin! Please, attend my dinner on Friday!
Do you have any new idea for you film? Anyway, Nicolas Winding Refn, we can talk about it during the dinner!
Hi! How is your childhood traumas, Sigmund Freid? Don't tell me, we will have this chat at the dinner!
Good to see you again, Grandmother! How is your sugar level?
Jesus Christ, how you even manage your activism in 70s while being a person of color? Very good topic for the dinner you are invited to, Martin Luther King Jr.!
```
