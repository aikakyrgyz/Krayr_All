
# Sequence Assignment, Parallel/Tuple/list assignment

x, y = 1, 2
print(x) # 1
print(y) # 2

# swap two value without using temporary variable

x, y = y, x

#############

l, m, (n,o) = (1, 2, [3, 4])

print(l, m, n, o) # 1 2 3 4

#############

a, *b, c = [1, 2, 3, 4, 5]

print(a, b, c) # 1 [2, 3, 4] 5

############

# *a, *b, c = [1, 2, 3, 4, 5]
#
# print(a, b, c) # SyntaxError: multiple starred expressions in assignment

############

l, (*m, n), *o = (1, ['a', 'b', 'c'], 2, 3, 4)
print(l, m, n, o) # 1 ['a', 'b'] c [2, 3, 4]

##################################### ITERATING OVER values in a list/tuple ##############

# two ways
# 1 st way: use indexing
# 2 nd way: just do the for loop

# 1st way
l = [1, 2, 3, 4, 5]

for i in range(len(l)):  # for i in range(5):
    print(l[i], end = ' ') # 1 2 3 4 5

print() # new line

# 2nd way

for num in l:
    print(num, end = ' ') # 1 2 3 4 5

####################################

x = ['a', 'b']
y = ['a', 'b']



# == and is

# the == operator determines whether two references refer to objects that store the same internal values

# the is operator determines whether two references refer to the same object

# note: lists are mutable

print(x is y) # False # pointing to the same object ?
print(x == y) # True  # they have the same value?
print(x[0] is y[0]) # True
print(x[1] is y[1]) # True
print(x[0] == y[0]) # True
print(x[1] == y[1]) # True

y[0] = 'c'
print(x) ## ['a', 'b']
print(y) ## ['c', 'b']


#################### pointing to the same object #########


x = ['a', 'b']
y = x

print(y) #['a', 'b']
print(x is y) # True


y[0] = 'c'
print(x) # ['c', 'b']
print(y) # ['c', 'b']

print(x[0] is y[0]) # True
print(x[1] is y[1])  # True
print(x[0] == y[0]) # True
print(x[1] == y[1]) # True


############ Conditional Statements and Ternary Operator ########


x = None

if x == None:
    y = 0
else:
    y = 1

# same as

y = 0 if x == None else 1

l = [1, 2]

# Syntax: TrueResult if test else FalseResult

x = 5
y = 10
min = 0

if x <=y:
    min = x
else:
    min = y

min = (x if x<=y else y)

print(min) # 5

###################
a = 10
if a % 2 == 0: # gives the remainder of a/2
    print(a, 'is even')
else:
    print(a, 'is odd')

# same as

print(a, ('is even' if a % 2 == 0 else 'is odd')) # 10 is even

print(str(a) + ' is ' + ('even' if a % 2 == 0 else 'odd'))

print(f"{a} is {'even' if a % 2 == 0 else 'odd'}")

########################
#
# if l == [1, 2]:
#     y = 3 * 5
# else:
#     y = 10
#
# y = 3*5 if l == [1, 2] else 10
# print(y) # 15
#
# # difference between None and empty data types
# print(type('')) # <class 'str'>
# print(type(None)) #<class 'NoneType'>
#
# print(type([])) # <class 'list'>


################


# pass

def func():
    pass

def func(): pass

x = 10
l = [1, 2, 3, 4, 5]

# in is an operator for lists and tuples that check whether or not the variable is inside the list/tuple
# in returns a bool -> True or false
################
if x in l: # if False
    pass
else:
    print(x, ' is not in ', l) # 10  is not in  [1, 2, 3, 4, 5]
################

if x not in l:
    print(x, ' is not in ', l) # 10  is not in  [1, 2, 3, 4, 5]


x = 'string'
x = 5

if type(x) == int:
    pass
else:
    print(x + 'concatenating')


# continue statement goes back to the beginning of the loop

x = 0
for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num, end = ' ') # 1 2 3 4 6 7 8 9 10

print(x)

 #1 2 3 4 1 2 3 4 5 6 7 8 9 10

for num in range(1, 11):
    if num == 5:
        for num in range(1, 11):
            print(num, end = ' ')
    else:
        print(num, end = ' ')
 # 1 2 3 4 1 2 3 4 5 6 7 8 9 10 6 7 8 9 10

print()
apple = 'apple'
for letter in apple:
    if letter == 'p':
        continue
    print(letter, end = '') # ale  # this line is ignored when letter is 'p'





