
# # Variables:
# name = "Taylor"
# age = 30
# gender = "male"


# # Impliment

# print(f'Hi {name}. You are {age} years old!')

# # string indexing [start, stop, step]

# indexText = 'Hi taylor what beer do you like?'

# print(indexText[0::2])

# # Immutability
# # You cannont reasign a part or index of a string once created. You can assign the whole new value as a reassignment. This is the concept of immutability.

# #Build in Functions + Methods

# # Length len()
# lengthTest = "this is a test string"
# print(len(lengthTest))

# # Exersize Type Conversion
# birth_year = int(input('what year were you born?'))

# age = 2020 - birth_year
# print(birth_year)

# print(f'Your age is {age} years old!')

# # Password Checker
# userName = input('Hi, please enter your user name: ')
# password = input(f'Thank you {userName}, please enter a password.')

# print(f'{userName} your password ***** is {len(password)} characters long.')

# # Lists
# cart_items = [
#     'thing 1',
#     'thing 2',
#     'thing 3',
# ]

# new_cart = cart_items[:]  # copies items
# print(new_cart)

#  Matrix arr in an arr

# list_one = [1, 2, 3]
# list_two = [4, 5, 6]

# list_one.append(list_two[2])

# print(list_one)

# Removing Items pop() you can index the pop


# ecersize logical operators:
# is_magician = True
# is_expert = False

# if is_magician and is_expert:
#     print("you are a master magician")

# if is_magician and not is_expert:
#     print("at least youre getting there")

# if not is_magician:
#     print('you need magical powers')

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list_sum = 0

# for i in my_list:
#     list_sum += i

# print(list_sum)

#
# Find Duplicate Values

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# dupe_list = []
# for item in some_list:
#     if (some_list.count(item) > 1):
#         dupe_list.append(item)
# print(set(dupe_list))

# # Functions
# def say_hello(text):
#     return print(f'{text}')


# say_hello('blah blah blah')

# # Highest Even
# def highest_even(li):
#     high_num = 0
#     for number in li:
#         if (number % 2 == 0 and number > high_num):
#             high_num = number
#     return high_num


# # print(highest_even([10, 2, 3, 52, 8, 11]))

# x = 'hello'.replace

# print(x)

# # Classes
# class PlayerCharacter:
#     def __init__(self, name, age, wepon):
#         self.name = name
#         self.age = age
#         self.wepon = wepon

#     def attack(self, attack_type):
#         print(attack_type)


# player1 = PlayerCharacter('Taylor', 30, 'axe')

# player1.attack(player1.wepon)

# # Cat Excerise
# class Cat:
#     species = 'mamal'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# cat1 = Cat('fluffy', 4)
# cat2 = Cat('sprinkles', 15)
# cat3 = Cat('vinny', 2)


# def find_old_cat(*args):
#     old_cat = 0
#     for cat in args:
#         if (cat.age > old_cat):
#             old_cat = cat.age
#     return old_cat


# print(f'The oldest cat is {find_old_cat(cat1, cat2, cat3)} years old!')

# #Pets
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Vinny(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# my_cats = Simon("Simon", 20)

# from functools import reduce

# # 1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']


# def cap(item):
#     return item.upper()


# print(list(map(cap, my_pets)))


# # 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5, 4, 3, 2, 1]

# new_list = list(zip(my_strings, my_numbers))
# print(new_list.sort())

# 3 Filter the scores that pass over 50%
# scores=[73, 20, 65, 19, 76, 100, 88]


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

# # Lamda test

# my_list = [5, 4, 3]

# print(list(map(lambda item: item**2, my_list)))

# def generator_function(num):
#     for i in range(num):
#         yield i


# def fib(num):
#     a = 0
#     b = 1
#     for i in range(num):
#         yield a
#         a = b
#         b = a + b


# for i in fib(20):
#     print(i)
