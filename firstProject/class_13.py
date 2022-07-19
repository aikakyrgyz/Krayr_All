
# Wrapping up the types
# immutable == hashable
# mutable == unhashable
# mutable is opposite of immutable

# Immutable: string, tuple, integers, float, frozenset
# Mutables: dict, list, sets

# A value whose type is a tuple and whose elements are all immutables then this tuple is immutable.

t = (1, 2, [5, 4])
t[2][0] =1
print(t)

t = (1, 2, {'a': 1})
t[2]['b'] = 2
print(t)


# 9 functions you need to know: split, join, any, all, sum, min, max, zip, enumerate

# 1: split

# It is a string method
# The argument passed is the value you want to split the string by
# by default thes split value is space
# this method returns a list of splitted values
s = 'apple;banana;berry;melon'
print(s.split(';')) # ['apple', 'banana', 'berry', 'melon']

s = 'yes--no'
print(s.split('--'))

line = 'Hello and today we are happy'
words = line.split()
print(words) # ['Hello', 'and', 'today', 'we', 'are', 'happy']


# join
# it is a string method
# Syntax: separator.join(list)
line_combined_back = '-'.join(words)
print(line_combined_back) # Hello-and-today-we-are-happy

separator = ' *** '
print(separator.join(['apple', 'banana', 'berry', 'melon'])) # apple *** banana *** berry *** melon


# all
# function
# works for any type of an iterable

print(all([True, True, True, False, True]))

l_bools = [True, False, True, False, True]
print(all(l_bools)) # False

def is_even(num):
    if num%2==0:
        return True
    else:
        return False

evens_or_not = [is_even(num) for num in range(10)]
print(evens_or_not) # [True, False, True, False, True, False, True, False, True, False]

print(all(evens_or_not)) # False


print(all([is_even(num) for num in [2, 4, 6]]))  # True


# any
# at least one of the elements in the iterable must be True for any to return True

print(any(l_bools)) # True
print(any([False, False, False, True]))
print(any([False, False, False])) # False

print(any(('', '', ''))) # False
print(bool('')) # False
print(bool(1)) # True
print(bool('string')) # True

print(any([True for string in ['apple', 'banana', 'berry', 'apricot'] if string.startswith('a')]))# True
# [True, False, False, True
print(all([True if string.startswith('a') else False for string in ['apple', 'banana', 'berry', 'apricot']]))# True

print([True if string.startswith('a') else False for string in ['apple', 'banana', 'berry', 'apricot']]) # [True, False, False, True]


############## pseudo-code
# all

def all(iterable):
    for e in iterable:
        if e == False:
            return False
    return True

#####################

# any
def any(iterable):
    for e in iterable:
        if e == True:
            return True
    return False


# sum
# returns the sum of iterables

print(sum([1, 2, 3]))
print(sum((1, 2, 3)))
print(sum({1, 2, 3}))

print(sum([10, 20], 10)) # 40


def f(x, y):
    return x*y
print(f(1, 2))
# print(f(2)) # TypeError

def f(x, y = 0):
    return x*y
print(f(1, 2))
print(f(2))

def sum(iterable, initial_sum = 0):
    total = initial_sum
    for i in iterable:
        total+=i
    return total


def sum(iterable, initial_sum = 0):
    for i in iterable:
        initial_sum +=i
    return initial_sum

print(sum([1, 2, 3], 5)) # 11
# sum([1, 2, 3])
x = 0
x+=1
print(x)


# min
# we can pass any iterable
# list of arguments
print(min([1, 3, 5, 0])) # 0
print(min(1, 3, 5, 0)) #0
print(min((1, 100, -3))) # -3
print(min('A', 'w')) # A

print(min('ABC', 'xyzw')) # ABC
print(min('ABCDF', 'xyzw', key = lambda x: len(x))) # xyzw

print(min([1, 2, 3], [5, 6, 7])) # 1 2 3
print(min([1, 2, 5], [1, 2, 6])) # 5 < 6
print(min([1, 2, 3, 4], [1, 2, 3])) # len([1, 2, 3, 4]) > len([1, 2, 3])

print(min([1, 4, 5], [1, 3, 10], key = lambda l: l[2])) # [1, 4, 5]

# zip

# it takes some number of iterables and zips them together
# used when you want to iterate in parallel fashion

z = zip([1, 2, 3], [4, 5, 6])
print(z) # <zip object at 0x7fe6402337c0>
print(list(z))
z = zip([1, 2, 3])
print(list(z))
z = zip([1, 2, 3], [1, 2, 3], [1, 2, 3])
print(list(z))
z = zip('ABC', [1, 2, 3])
print(dict(z)) # {'A': 1, 'B': 2, 'C': 3}
z = zip('ABC', [1, 2, 3], ['one', 'two', 'three']) # [('A', 1, 'one'), ('B', 2, 'two'), ('C', 3, 'three')]
print(tuple(z))


z = zip([1, 2, 3], [4, 5, 6])
print(list(z)) # [(1, 4), (2, 5), (3, 6)]
print(list(z)) # []

for country, index in zip(['Poland', 'Germany'], [5, 99]):
    print(country, index)

z = zip([1, 2], [5, 6, 7])
print(list(z))# [(1, 5), (2, 6)]

z = zip([5, 6, 7], [1, 2])
print(list(z))

# function that compares two strings and return if str1 > str2
# 'ABC' > 'abc' -> False

def greater_than(str1 : str , str2: str) -> bool: # str1 > str2 ?
    if min(str1, str2) == str1:
        return False
    return True

# alternative way

print(greater_than('ABC', 'abc')) # False


def greater_than(str1 : str , str2: str) -> bool: # str1 > str2 ?
    for x, y in zip(str1, str2):
        if x != y:
            return x > y
    return len(str1) > len(str2)

print(greater_than('ABCD', 'ABC')) # False


#
# # tuple comprehension
# t = (num for num in range(10)) # creates a generator
# print(tuple(t)) # <generator object <genexpr> at 0x7ffc9e214eb0>
# for n in t:
#     print(n)
# l = (num for num in range(1000000000000000000000000))
#

print()


# enumerate
# default starting value is zero
l = ['apple', 'banana', 'berry']
e = enumerate(l)
print(list(e)) # [(0, 'apple'), (1, 'banana'), (2, 'berry')]
e = enumerate(l)
print(dict(e)) # {0: 'apple', 1: 'banana', 2: 'berry'}
e = enumerate(l, 1)
print(list(e))

for i in range(len(l)):
    print((i+1, l[i]))
# (1, 'apple')
# (2, 'banana')
# (3, 'berry')

for i, e in zip(range(1, 4), l):
    print((i, e))












