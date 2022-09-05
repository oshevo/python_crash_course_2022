# Chapter 4

This chapter will explain *How to work with lists* using loops.

## Exercise 4-1 Pizzas

```python
pizzas = ['peperoni', 'capricciosa', 'hawaiian']

for pizza in pizzas: # initialing a loop
    # print (pizza)
    print(f'i LOVE {pizza} pizza!')

print('\ni really like pizza!')
```

**OUTPUT:**

```
i LOVE peperoni pizza!
i LOVE capricciosa pizza!
i LOVE hawaiian pizza!

i really like pizza!
```

## Exercise 4-2 Animals

```python
animals = ['lion', 'puma', 'panther', 'cheetah', 'leopard', 'jaguar']

for animal in animals:
    # print(animal)
    print(f'{animal.title()} is a member of Felidae.')

print('\nAll of them can be refered as "cats".')
```

**OUTPUT:**

```
Lion is a member of Felidae.
Puma is a member of Felidae.
Panther is a member of Felidae.
Cheetah is a member of Felidae.
Leopard is a member of Felidae.
Jaguar is a member of Felidae.

All of them can be refered as "cats".
```
## Exercise 4-3 Counting to Twenty

```python
for value in range(1, 21):
    print(value)
```

**OUTPUT:**

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```

## Exercuse 4-4 One Million

```python
millions = list(range(1, 1000001))

for million in millions:
    print(million)
```

**OUTPUT:**

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
...
999997
999998
999999
1000000
```

## Exercise 4-5 Summing a Million

```python
millions = list(range(1, 1000001))

print(min(millions))    # printing a minimum value of the list
print(max(millions))    # printing a maximum value of the list
print(sum(millions))    # printing a sum of the list
```

**OUTPUT:**

```
1
1000000
500000500000
```

## Exercise 4-6 Odd Numbers

```python
odd_numbers = list(range(1, 20, 2))    # creating a list of odd numbers

for odd_number in odd_numbers:
    print(odd_number)
```

**OUTPUT:**

```
1
3
5
7
9
11
13
15
17
19
```

## Exercise 4-7 Threes

```python
threes = list(range(3, 33, 3))   # creating a list of numbers that multiple of 3

for three in threes:
    print(three)
```

**OUTPUT:**

```
3
6
9
12
15
18
21
24
27
30
```

## Exercise 4-8 Cubes

```python
cubes = []     # crealing an empty list 

for value in range(1, 11):
    cubes.append(value **3)    # appending values to the list

for cube in cubes:
    print(cube)
```

**OUTPUT:**

```
1
8
27
64
125
216
343
512
729
1000
```

## Exercise 4-9 Cube Comprehension

```python
cubes = [value **3 for value in range(1, 11)] # creating a list via List Comprehension
print(cubes)
```

**OUTPUT:**

```
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

## Exercise 4-10 Slices

```python
cubes = [value **3 for value in range(1, 11)]
print(cubes)

print('\nThe first three items in the list are:')
print(cubes[:3])    # printing sliced first 3 elements

print('Three items from the middle of the list are:')
print(cubes[2:5])    # printing sliced middle 3 elements

print('The last three items in the list are:')
print(cubes[-3:])    # printing sliced last 3 elements
```

**OUTPUT:**

```
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

The first three items in the list are:
[1, 8, 27]
Three items from the middle of the list are:
[27, 64, 125]
The last three items in the list are:
[512, 729, 1000]
```

## Exercise 4-11 My Pizzas, Your Pizzas

```python
pizzas = ['peperoni', 'capricciosa', 'hawaiian']

for pizza in pizzas:
    # print (pizza)
    print(f'i LOVE {pizza} pizza!')

print('\ni really like pizza!')

friend_pizzas = pizzas[:]    # copying the list

pizzas.append('margarita')    # adding a new element to the list
friend_pizzas.append('grana padano')

print('\nMy favorite pizzas are:')
print(pizzas)

print('My friend’s favorite pizzas are:,')
print(friend_pizzas)
```

**OUTPUT:**

```
i LOVE peperoni pizza!
i LOVE capricciosa pizza!
i LOVE hawaiian pizza!

i really like pizza!

My favorite pizzas are:
['peperoni', 'capricciosa', 'hawaiian', 'margarita']
My friend’s favorite pizzas are:,
['peperoni', 'capricciosa', 'hawaiian', 'grana padano']
```

## Exercise 4-12 More Loops

```python
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('cannoli') 
friend_foods.append('ice cream')

print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)
```

**OUTPUT:**

```
My favorite foods are:
pizza
falafel
carrot cake
cannoli

My friend's favorite foods are:
pizza
falafel
carrot cake
ice cream
```

## Exercise 4-13 Buffet

```python
menu = ('borshch', 'varenyky', 'nalysnyky', 'holubtsi', 'syrnyk')    # creating a tuple

print('Our menu:')
for dish in menu:
    print(dish)

# menu[1] = 'kapusniak'    # error attempt

menu = ('borshch', 'varenyky', 'banosh', 'salo', 'syrnyk')    # reassingning a tuple

print('\nOur new menu:')
for dish in menu:
    print(dish)
```

**OUTPUT:**

```
Our menu:
borshch
varenyky
nalysnyky
holubtsi
syrnyk

Our new menu:
borshch
varenyky
banosh
salo
syrnyk
```

## Exercise 4-14 PEP 8

Well, given link into the book doesn't exist anymore. Here is actual one for [the PEP 8](https://peps.python.org/pep-0008/).

Scroll through it, there are a lot of interesting stuff.

## Exercise 4-15 Code Review

![On the image, you can't see the ruler lines, are demonstrated](/Users/olhababenko/Desktop/screenshot.jpeg 'Screenshot of the Workspace')
*I added the vertical rulers for three points: 80, 120, 160.*