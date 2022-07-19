


l = [10, 20, 30, 40]

l = [10, 20]
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def problem3(l):
    for i in range(len(l)): # range(len(l)) -> [0, 1, 2, 3]
     # first loop: l[0] -> 10, # second loop: l[1] -> 20
        if i == 0 or i == len(l)-1:
            continue
        print(l[i])

    ########################
    # for i in l:
    #     print(i)

problem3(l)


# count(5, [1, 2, 3, 5, 6, 7, 5, 9, 5])


def count(num, l):
    count = 0
    for n in l:
        if n == num:
            count += 1
    return count

print(count(5, [1, 2, 3, 5, 6, 7, 5, 9, 5]))

# indexes(5, [1, 2, 3, 5, 6, 7, 5, 9, 5]) -> [3, 6, 8]
# range(len(l)) -> [0, 1, 2, 3, 4, 5, 6, 7, 8]


def indexes(num, l):
    list_r = []
    for i in range(len(l)):
        if num  == l[i]:
            list_r.append(i)
    return list_r


list_returned = indexes(5, [1, 2, 3, 5, 6, 7, 5, 9, 5])
print(list_returned)


# 2D list

# l = [[1, 2, 3, 4], [5, 6, 7, 8]]
# for list_ in l:
#     for num in list_:
#         print(num)
#
# for list_ in l:
#     print(list_)

l = [1, 2, 3, [100, 200, 300], 90, 80, 99, [0, 0, 0], (0, 5, 43), (1, )]
for element in l:
    if type(element) == list or type(element) == tuple:
        for num in element:
            print(num, end = ' ')
    else:
        print(element, end = ' ')
print()
# 1 2 3 100 200 300 90 80 99 0 0 0 0 5 43 1


################### SET ##################

# lists allow you to have duplicates within them
# sets stores values where none are duplicate

s = {1, 2, 3}
s = set() # creating an empty set not  s = {} -> this would create a dictionary

print(type(s)) # set
print(s)


############ PYTHON SHELL ################
'''
>>> x = [1, 2]
>>> y = [1, 2]
>>> x is y
False
>>> x == y
True
>>> x[0] == y[0]
True
>>> x[0] is y[0]
True
>>> x = [1, 2]
>>> y = x
>>> y
[1, 2]
>>> x is y
True
>>> x[0] == y[0]
True
>>> x[0] is y[0]
True
>>> x = [1, [2, 5]]
>>> x
[1, [2, 5]]
>>> x[0]
1
>>> x[1]
[2, 5]
>>> x = y
>>> y
[1, 2]
>>> x = [1, [2, 5]]
>>> y = x
>>> y
[1, [2, 5]]
>>> x is y
True
>>> y[0] = 100
>>> y[0]
100
>>> y
[100, [2, 5]]
>>> x
[100, [2, 5]]
>>> import copy from copy
  File "<stdin>", line 1
    import copy from copy
                ^
SyntaxError: invalid syntax
>>> from copy import copy
>>> x = [1, [2, 5]]
>>> y = copy(x)
>>> y
[1, [2, 5]]
>>> x is y
False
>>> x[1]
[2, 5]
>>> y[1]
[2, 5]
>>> x[0] is y[0]
True
>>> x[0][0] is y[0][0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> x[1][0] is y[1][0]
True
>>> from copy import deepcopy
>>> x = [1, [2, 5]]
>>> y = deepcopy(x)
>>> y
[1, [2, 5]]
>>> x is y
False
>>> x[1] is y[1]
False
>>> x[1] == y[1]
True
>>> y[1][1] = 100
>>> y
[1, [2, 100]]
>>> x
[1, [2, 5]]
>>> 
>>> x == y
False
>>> x[1] == y[1]
False
>>> x[0] == y[1]
False
>>> x = [1, 2]
>>> y = [1, 2]
>>> x[0] is y[0]
True
>>> x[0] = 100
>>> x
[100, 2]
>>> y
[1, 2]
>>> x = [32432432543543534, 2]
>>> y = [32432432543543534, 2]
>>> x is y
False
>>> x[0] == y[0]
True
>>> x[0] is y[0]
False
>>> 
>>> 
>>> s = {1, 2, 3}
>>> 1 in s
True
>>> 2 in s
True
>>> 10 in s
False
>>> l = [1, 2, 3, 4, 5]
>>> string = '1'
>>> int(string)
1
>>> set(l)
{1, 2, 3, 4, 5}
>>> l = set(l)
>>> l
{1, 2, 3, 4, 5}
>>> type(l)
<class 'set'>
>>> t = (1, 2)
>>> t = set(t)
>>> t
{1, 2}
>>> type(t)
<class 'set'>
>>> set(range(0,10))
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> duplicates = [1, 1, 2, 2, 3, 3, 4, 4]
>>> duplicates = set(duplicates)
>>> duplicates
{1, 2, 3, 4}
>>> duplicates.add(5)
>>> duplicates
{1, 2, 3, 4, 5}
>>> # sets are mutable just like lists
>>> # methods of sets
>>> s1 = {1, 3, 5, 7, 9}
>>> s2 = {2, 4, 6, 10}
>>> s1|s2
{1, 2, 3, 4, 5, 6, 7, 9, 10}
>>> s[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> # sets are not ordered
>>> # lists are ordered
>>> l = [1, 2, 3, 5]
>>> 
>>> # | - union
>>> # & - intersection
>>> s1 = {1, 2, 3, 4}
>>> s2 = {5, 7, 2}
>>> s1&s2
{2}
>>> # - : difference
>>> s1 = {1, 3, 5, 7}
>>> s2 = { 2, 5, 8, 11}
>>> s1 - s2
{1, 3, 7}
>>> s2 - s1
{8, 2, 11}
>>> # ^ - symmetric difference
>>> s1^s2
{1, 2, 3, 7, 8, 11}
>>> s1.union(s2)
{1, 2, 3, 5, 7, 8, 11}
>>> s1.difference(s2)
{1, 3, 7}
>>> x +=1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> x = 0
>>> x +=1
>>> x = x + 1
>>> # ------
>>> s = set()
>>> s
set()
>>> len(s)
0
>>> s|={3, 4}
>>> s
{3, 4}
>>> s = {1, 2}
>>> s|={3, 4}
>>> s
{1, 2, 3, 4}
>>> s = s|{3,4}
>>> s
{1, 2, 3, 4}
>>> s = {1, 2}
>>> s = {1, 2}
>>> s_union = s|s
>>> s
{1, 2}
>>> s_union
{1, 2}
>>> s = {1, 2}
>>> s2 = {1, 5}
>>> s_union = s|s2
>>> s_union
{1, 2, 5}
>>> # add method -> append values at the end of the set
>>> s[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> s.add({100, 200}
... 
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> s.add({100, 200})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> s.update({100, 200})
>>> s
{200, 1, 2, 100}
>>> s.add(999)
>>> s
{1, 2, 100, 999, 200}
>>> # use add when you want to add one value in the set
>>> # use append when you want to add more than one value in the set
>>> s.update([55, 66])
>>> s
{1, 2, 66, 100, 999, 200, 55}
>>> s.update((55, 66))
>>> ws
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ws' is not defined
>>> s
{1, 2, 66, 100, 999, 200, 55}
>>> # iterating set
>>> for num in s:
...     print(s)
... 
{1, 2, 66, 100, 999, 200, 55}
{1, 2, 66, 100, 999, 200, 55}
{1, 2, 66, 100, 999, 200, 55}
{1, 2, 66, 100, 999, 200, 55}
{1, 2, 66, 100, 999, 200, 55}
{1, 2, 66, 100, 999, 200, 55}
{1, 2, 66, 100, 999, 200, 55}
>>> for num in s:
...     print(num)
... 
1
2
66
100
999
200
55
>>> for num in s:
...     print(num)
... 
1
2
66
100
999
200
55
'''

