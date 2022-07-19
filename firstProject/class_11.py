

# List Comprehensions continued


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = [x**2 for x in a if x%2==0]

print(even_squares) #[4, 16, 36, 64, 100] = [2**2, 4**2, 6**2 ...]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
one_D = [r for row in matrix for r in row]
print(one_D) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


one_D =  []
for row in matrix:
    for r in row:
        one_D.append(r)

print(one_D)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_squared = [[x**2 for x in row] for row in matrix]

print(matrix_squared) # [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

############### same process but with for loops ################
matrix_squared = []
for row in matrix:
    inner_list = []
    for num in row:
        inner_list.append(num**2)
    matrix_squared.append(inner_list)
print(matrix_squared) # [[1, 4, 9], [16, 25, 36], [49, 64, 81]]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x>4 if x%2 ==0]
print(b) # [6, 8, 10]
# this comprehension is equivalent
c = [x for x in a if x>4 and x%2 ==0]
print(c)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered_m = [[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]
print(filtered_m)# 1st loop: 1+ 2+ 3= 6 -> ignored
                # 2nd loop: 4 + 5 + 6 = 15 -> sum(row) >=10 ->  [6]
                # 3rd loop: 7 + 8 + 9 = 24 -> sum(ro) >=10 -> [9]
                # result: [[6], [9]]


# Dict comprehension

# Syntax: {key: value for key, value in d.items() if test}
# Syntax: {key: value for x in some_list}

l = ['one', 'two', 'three', 'four', 'five']

str_len = {key: len(key) for key in l} # {'one': 3, 'two': 3, 'three': 5, 'four': 4, 'five': 4}
print(str_len)


str_len = {key: len(key) for key in l if key.startswith('t')}
print(str_len) # {'two': 3, 'three': 5}

# notice this is a set comprehension
x = {char for word in ['one', 'two', 'three'] for char in word if char not in 'aeiou'}
print(x) # sets are not sorted

# the same comprehension but in for loop

x = set()
for word in ['one', 'two', 'three']:
    for char in word:
        if char not in 'aeiou':
            x.add(char)
print(x)

# the same comprehension but still using comprehension

x = set()
for word in ['one', 'two', 'three']:
    x = x.union({char for char in word if char not in 'aeiou'})
    # end of 1st loop: x = {'n'}
    # end of 2nd loop: x = {'t', 'w'} -> union -> x = {'n', 't', 'w'}
    # end of 3rd loop: x = {'t', 'h', 'r'} -> union -> x = {'w', 'h', 'n', 'r', 't'}
print(x)


d = {word: {char for char in word} for word in ['one', 'two', 'three']}

print(d) # {'one': {'e', 'o', 'n'}, 'two': {'w', 'o', 't'}, 'three': {'h', 'e', 'r', 't'}}

# tuple comprehension
# Tuple comprehension are special because they do not return a tuple
# They return generator
# Why generator are used? They are space efficient
# Note: it becomes exhausted when you iterate through all values

t_generator = (num for num in [1, 2, 3])
print(t_generator) # <generator object <genexpr> at 0x7fdebe582580>

t_as_tuple = tuple(t_generator) # list(t_generator)
print(t_as_tuple) # (1, 2, 3)


for x in t_generator:
    print(x)

t_g = (char for char in 'word')
for char in t_g: # for char in ('w', 'o', 'r', 'd')
    print(char)
print(tuple(t_g)) # ()

for char in t_g:
    print(char)

##################################

x = 'A'
for x in range(5): # 0, 1, 2, 3, 4
    pass
print(x) # 4
#print(num)

x = 'A'
y = [x for x in range(5)] # when you do the list comprehension, it creates its own local scope

print(x) # A


def f():
    function_variable = 2

# print(function_variable) -> NameError

# DICTIONARY CONSTRUCTORS

d = {1: 'one', 2: 'two'}
d = dict(a=1, b=2, c=4)
print(d) # {'a': 1, 'b': 2, 'c': 4}

print(list(d.values())) # [1, 2, 4]
print(list(d.keys())) #['a', 'b', 'c']
print(list(d.items())) # [('a', 1), ('b', 2), ('c', 4)]

d = dict([('a', 1), ('b', 2), ('c', 4)]) # list of 2-element tuples
print(d) # {'a': 1, 'b': 2, 'c': 4}
d = dict([['a', 1], ['b', 2], ['c', 4]]) # list of 2-element lists
print(d)


#{'a': 1, 'b': 2, 'c': 4}
# make a copy with comprehensions

d_copy = {key: value for key, value in d.items()}
print(d_copy)

# copy by using a constructor
d_copy = dict(d)

d_copy = dict(d.items())










