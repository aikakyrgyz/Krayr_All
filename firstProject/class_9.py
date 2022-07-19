
# dictionaries
"""
>>> d = {}
>>> type(d)
<class 'dict'>
>>> s = set()
>>> d = {'a': 1, 'b': 2}
>>> d = {'a': 1, 'b': 2}
>>> users = {'Aika': 'Senior', 'Alisa': 'Junior', 'Blake':'Freshman'}
>>> users['Aika']
'Senior'
>>> d['b']
2
>>> # dictionaries are unordered
>>> d = {'a': 1, 'a':2}
>>> d
{'a': 2}
>>> # every key in a dictionary must be unique
>>> # every key must be of an immutable type
>>> d = {[1, 2]: 'Aika'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> # access the value by specifying the key
>>> # empty ditionary
>>> d = {]
  File "<stdin>", line 1
    d = {]
         ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> d = {}
>>> d = {'food': {'bread': 2, 'egg': 3}}
>>> d['food']
{'bread': 2, 'egg': 3}
>>> # values can be mutable or immutable and different keys can have the same value
>>> d = {'bread': 3, 'egg': 3}
>>> d['bread']
3
>>> d['egg']
3
>>> d = {'food': {'bread': 2, 'egg': 3}}
>>> # d = {key:value}
>>> d['food']['bread']
2
>>> d['food']['egg']
3
>>> l = [1, 3, [5, 6], 0]
>>> l[2][0]
5
>>> # dictionary methods
>>> d.has_key('food')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'has_key'
>>> d.get('food')
{'bread': 2, 'egg': 3}
>>> d['food']
{'bread': 2, 'egg': 3}
>>> 'food' in d
True
>>> 'bread' in d['food']
True
>>> 'nonexistant' in d
False
>>> d.keys()
dict_keys(['food'])
>>> d = {'food': {'bread': 2, 'egg': 3}, 'car': 5}
>>> d.keys()
dict_keys(['food', 'car'])
>>> d.values()
dict_values([{'bread': 2, 'egg': 3}, 5])
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> d.keys()
dict_keys(['a', 'b', 'c'])
>>> d.values()
dict_values([1, 2, 3])
>>> len(d)
3
>>> # adding values to the dictionary
>>> d['d'] = 4
>>> d
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> d = {'food': {'bread': 2, 'egg': 3}, 'car': 5}
>>> d['food']['carrot'] = 1
>>> d
{'food': {'bread': 2, 'egg': 3, 'carrot': 1}, 'car': 5}
>>> # delete pair
>>> del d['car']
>>> d
{'food': {'bread': 2, 'egg': 3, 'carrot': 1}}
>>> {'a': 1, 'b': 2, 'c': 3, 'd': 4}
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> del ['a']
  File "<stdin>", line 1
    del ['a']
         ^
SyntaxError: cannot delete literal
>>> del['a']
  File "<stdin>", line 1
    del['a']
        ^
SyntaxError: cannot delete literal
>>> del d['a']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'a'
>>> d
{'food': {'bread': 2, 'egg': 3, 'carrot': 1}}
>>> d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> del d['a']
>>> d
{'b': 2, 'c': 3, 'd': 4}
>>> del d['c']
>>> d
{'b': 2, 'd': 4}
>>> del d[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 4
>>> d = {'food': ['eggs', 'carrots', 'bread']}
>>> languages = {'Python': 'Guido van Rossum', 'Perl': 'Larry Wall'}
>>> languages
{'Python': 'Guido van Rossum', 'Perl': 'Larry Wall'}
>>> language = 'Python'
>>> creator = languages[language] # languages['Python']
>>> creator
'Guido van Rossum'
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d.keys():
...     print(key)
...
a
b
c
>>> for value in d.values():
...     print(value)
...
1
2
3
>>> for key, value in d.items():
...     print(key, value)
...
a 1
b 2
c 3
>>> d.keys()
dict_keys(['a', 'b', 'c'])
>>> type(d.keys())
<class 'dict_keys'>
>>> list(d.keys())
['a', 'b', 'c']
>>> list(d.values())
[1, 2, 3]
>>> list(d.items())
[('a', 1
"""

"""
month_numbers = {'Jan': 1, 'Feb': 2, 'Mar':3, 'Apr':4, 'May': 5,
                 1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5:'May'}
print(len(month_numbers)) # 10

print('The 3rd month is ' + month_numbers[3]) # The 3rd month is Mar
distance = month_numbers['Apr'] - month_numbers['Jan'] # 4 - 1 = 3 = distance
print('Apr and Jan are', distance, 'months apart') # Apr and Jan are 3 months apart

month_numbers['June'] = 6

print(month_numbers) # {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 'June': 6}

month_numbers['Jan'] = 0

print(month_numbers)

"""
########################

capitals = {'France': 'Paris', 'Italy': 'Rome', 'Japan': 'Kyoto'}

for key in capitals: # for key in capitals.keys()
    print('The capital of', key, 'is ', capitals[key])

# The capital of France is  Paris
# The capital of Italy is  Rome
# The capital of Japan is  Kyoto

for country, capital in capitals.items():
    print(f'The capital of {country} is {capital}')

cities = []
for value in capitals.values():
    cities.append(value)
print(cities, ' is a list of all cities') # ['Paris', 'Rome', 'Kyoto']  is a list of all cities

capitals['Japan'] = 'Tokyo'
print(capitals)


d1 = {'a': 1, 'b': 2}
d2 = {'c':3, 'd': 4}

# combine two dictionaries
d1.update(d2)
print(d1) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d1.update({'e':5, 'f':6})
print(d1) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# length of dict
print(len(d1))

# keys
print(d1.keys())

# values
print(d1.values())

# pairs
print(d1.items())

# combine two
d1.update(d2)

# check if the key is in dictionary
print('w' in d1) # False
print('a' in d1) # True

# return the value of the key

print(d1['a']) # 1

# return the value, with optional default value

print(d1.get('f')) # 6
print(d1.get('w')) # None

# if there is no key named 'w' then it will return the specified value 26
print(d1.get('w', 26)) # 26
# compare to this line

# print(d1['w']) # -> KeyError: 'w'

# change or add a pair (they both have the same syntax)

#change
d1['a'] = 0

# add
d1['s'] = 24

print(d1)

# delete the pair

del d1['s']


# DATA TYPES

# two types: mutable and immutable

# MUTABLES: list, dictionary, sets

# IMMUTABLES: tuples, strings, integers, floats

# ITERABLES: lists, tuples, sets, dictionaries, strings

l = [1, 2, 3, 4, 5]
l2 = []

for num in l:
    l2.append(num)

print(l2) # [1, 2, 3, 4, 5]

# list comprehesnsion: iterating over an iterable

# syntax
# [return_value for elem in iterable if test]
# [0, 2, 4, 6, 8, 10]

l = [num for num in range(0, 11) if num%2 == 0]
# range(0, 11) -> [0, 1, 2, 3, 4, 5, .... 10]
print(l) # [0, 2, 4, 6, 8, 10]

l = []
for num in range(0, 11):
    if num % 2 == 0:
        l.append(num)


l = [num**2 for num in range(0, 11) if num%2 ==0]
print(l) # [0, 4, 16, 36, 64, 100]

# num**2 -> num^2


l = [2*char for char in 'paris' if char in 'aoeiuy']
print(l) # ['aa', 'ii']

def is_odd(n):
    if not n%2==0:
        return True

l = [num for num in range(0, 11) if is_odd(num)]
print(l) # [1, 3, 5, 7, 9]

l = [(x, y) for x in range(11) if x %2 == 0 for y in range(11) if y%3 == 0]
print(l)
# [(0, 0), (0, 3), (0, 6), (0, 9), (2, 0),
#   (2, 3), (2, 6), (2, 9), (4, 0), (4, 3), (4, 6), (4, 9), (6, 0), (6, 3), (6, 6), (6, 9), (8, 0), (8, 3), (8, 6), (8, 9), (10, 0), (10, 3), (10, 6), (10, 9)]

l = [(x, y) for x in range(3) for y in range(5)]
print(l)

l = []
for x in range(3):
    for y in range(5):
        l.append((x, y))
print(l)



x = [1, 2, 3]
y = ['a', 'b', 'c']

l = [(i, j) for i in x for j in y]
print(l)

outer_list = [[1, 2], [3, 4], [5, 6]]
# l = [j for i in x for j in i]
print(l)

l = [j for inner_list in outer_list for j in inner_list]
print(l)

# equivalent

l = []
for inner_list in outer_list:
    for j in inner_list:
        l.append(j)
print(l) # [1, 2, 3, 4, 5, 6]


# hw question 2

# between -> 2 parameters
# return a reference to a function that has one parameter -> return function but do not call it
# inclusive

# Ex: 18 and 20
# 19 -> True
# 20 -> True

def between(a, b):
    def yes_in_between(c):
        if a <= c <= b:
            return True
        else:
            return False
    return yes_in_between

college_age = between(18, 20)
print(college_age(19)) # True

senior = between(60, 100)
print(senior(70))
print(senior(21)) # False








