#
# # Lists and Tuples
#
#
# # data structures: used to store some data, like a container
# # tuple
# # list
# # dict
# # range: also a data structure, because it stores a sequence of numbers
# # string: also a data structure, because it stores a collection of characters
#
#
# # tuple
# cannot change it, meaning no deletion, no addition of new elements
# can only access an element
#
# # point = (x, y)
# # cartesian coordinates, 2 - D
#
# point = (1, 2)
#
# t = ('Apple', 1, 'Banana', 5, 6)
#
# one_value_tuple = (5, )
# print(one_value_tuple)
# print(point)
#
# print(type(point)) # <class 'tuple'>
#
# print(len(point)) # 2
#
# print(len(t)) # 5
#
# string = 'word'
# print(len(string)) # 4
#
# # accessing an element in a tuple using indexing
# # indexing starts from 0
#
# # indexing can also start from the end with -1
#
# # (1, 2, 3, 4, 5)
# # [-5,-4,-3,-2,-1)
#
#
# # sequence assignment
# x = 5
# x, y = 5, 7
# print(x) # 5
# print(y) # 7
#
# x, y = point # x, y = 1, 2
# x, y = (1, 2)
# print(x) # 1
# print(y) # 2
#
# t = ('word', 1, 3)
# word, x, y = t # word, x, y = ('word', 1, 3)
#
# a = 10
# b = 20
#
# print(a)
# print(b)
#
# a, b = b, a
#
# print(a) # 20
# print(b) # 10
#
# name = 'Boy'
# a, b, c = 'Boy'
# print(a) # B
# print(b) # o
# print(c) # y
#
#
# r = range(3) # [0, 1, 2]
# a, b, c = r
# print(a) # 0
# print(b) # 1
# print(c) # 2
#
# # a sequence of elements is called iterable
#
# # whenever you have an iterable on the right side, you can do a sequence assignment
#
# # iterating
# # for i in range(6):
# #     print(i)
#


############# LISTS ###################

# List - is a sequence of elements that you expect to change over its lifetime.

# ex: if you want to store usernames of each user that visits the website

l = [1, 2, 3, 4, 5]
print(type(l)) # <class 'list'>

# length of the list
print(len(l)) # 5

nothing = []
print(len(nothing)) # 0

# access the values within the list by using index
print(l[2]) # 3

print(l[0]) # 1


# change the value in the list

print(l) # [1, 2, 3, 4, 5]
l[0] = 100
print(l) # [100, 2, 3, 4, 5]

l[-1] = 500
print(l) #[100, 2, 3, 4, 500]

# adding a new element to the end of the list: append
# list.method_name()

# the list method always changes/saves the list

l.append(6)
print(l) # [100, 2, 3, 4, 500, 6]

l.append([1, 2, 3])
print(l) #[100, 2, 3, 4, 500, 6, [1, 2, 3]]
# the last list [1, 2, 3] is one element
print(l[-1]) # [1, 2, 3]

l.append((1, 2, 3))
print(l) # [100, 2, 3, 4, 500, 6, [1, 2, 3], (1, 2, 3)]

l.append('John')
print(l) # [100, 2, 3, 4, 500, 6, [1, 2, 3], (1, 2, 3), 'John']


# add elements at the end of the list as separate elements
l = [1, 2, 3, 4, 5]

l.extend([1, 2, 3])

print(l) # [1, 2, 3, 4, 5, 1, 2, 3]
print(l[-1]) # 3

l = [1, 2, 3, 4, 5]
l += [1, 2, 3] # l = l + [1, 2, 3]
print(l) # [1, 2, 3, 4, 5, 1, 2, 3]

x = 0
x +=1 # x = x + 1
x -=1
x *=2


# delete an elements inside a list
l = [1, 2, 3, 4, 5]
del l[0]
print(l) # [2, 3, 4, 5]

del l[-1]
print(l) # [2, 3, 4]

# range objects

r = list(range(1, 10))
print(r) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# type casting
point = (5, 2, -1) # tuple

point = list(point)

print(point) # [5, 2, -1]

# another way

point = list((5, 2, -1))

# You can type cast any iterable object with a list constructor

# constructor -> list() -> constructs you a list


letters = list('Alexandra')
 # note: a string is an iterable

print(letters) # ['A', 'l', 'e', 'x', 'a', 'n', 'd', 'r', 'a']

print(list([1, 2, 3])) # [1, 2, 3]


# Slicing
word = 'apple'
print(word[0:3]) #app

# Slicing with lists and tuples

# range(start, end, step)
# range(start, end)
# range(end)
# note: the last number is not included
# [start, end)
l = list(range(0, 21, 2))
print(l) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

l = list(range(0, 21))
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

l = list(range(21))
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# by default the start is 0


x = list(range(0, 21, 2))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(x[0:5]) #[0, 2, 4, 6, 8]

print(x[4:-2]) # [8, 10, 12, 14, 16]
print(x[-5: 8]) # [12, 14]
print(x[-5:-1]) # [12, 14, 16, 18]

print(x[:5]) # [0, 2, 4, 6, 8]

print(x[4: ]) #[8, 10, 12, 14, 16, 18, 20]

print(x[:]) # copying the list

y = x[:]
print(y) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(x[2:9:2]) #[4, 8, 12, 16]

print(x[3:0:-1]) #[6, 4, 2]

print(x[3:0:-2])

print(x[::-1]) # [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]

y = x[::-1]
print(y) # [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]

print(x[3:2]) # -> []




x = [1, 2, 3]
print(x)
# # print(x[0:1]) # [1]
# # print(x[0:2]) # [1, 2]
#
print(x[-1:]) # [-3]
print(x[-1:0:-1]) # [3, 2]


# RECAP:
# use tuple when you know that you would not change it
# use list when you know that you will change it

# tuple : immutable(unchangable)
# list  : mutable (changable)

















