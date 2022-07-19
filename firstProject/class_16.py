country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Germany': 90, 'Australia': 90}

print(country['Poland'])
#print(country['USA'])

# d.get(key, default) -> returns the value in dictionary, or returns the default (that you specified) if the
# key is not in the dictionary -> equivalent to saying ( d[key] if k in d else default )
# print(country.get('Poland', 0))
# print(country.get('USA', 0))
# print(country)

# d.setdefault(key, default) -> returns the value d[key] in dictionary, if key is not in the dictionary
# then sets d[key] = default and then returns d[key]
# equivalent to

# if key in d:
#   return d[k]
# else
#   d[k] = default
#   return d[k]

print(country.setdefault('USA', 0)) # 0
print(country)


##########################
letters = ['a', 'x', 'b', 'c', 'c', 'w']
d = dict()
for l in letters:
    if l not in d:
        d[l] = 1
    else:
        d[l] += 1
print(d)
##########################

from collections import defaultdict
letters = ['a', 'x', 'b', 'c', 'c', 'w']
dd = defaultdict(int)
for l in letters:
    dd[l] += 1
print(d)

######################### if the default dictionary was not used ############
letters = ['a', 'x', 'b', 'c', 'c', 'w']
d = dict()
for l in letters:
    if l not in d:
        d[l] = int()
    d[l] +=1
print(d)
############################### another way ###########

letters = ['a', 'x', 'b', 'c', 'c', 'w']
d = dict()
for l in letters:
    d[l] = d.setdefault(l, 0) + 1
print(d)

# 1 st loop:
    # d = {}
    # d.setdefault('a', 0) + 1 = 0 + 1 = 1
    # d = {'a': 1}
# 2nd loop:
    # d = {'a':0}
    # d.setdefault('x', 0) + 1 = 0 + 1 = 1
    # d = {'a': 1, 'x': 1}
# 3rd loop
    # d = {'a': 1, 'x': 1}
    # d.setdefault('b', 0) + 1 = 0 + 1 = 1
    # d = {'a': 1, 'x': 1, 'b':1}
# 4th loop:
    # d = {'a': 1, 'x': 1, 'b':1}
    # d.setdefault('c', 0) + 1 = 0 + 1 = 1
    # d = {'a': 1, 'x': 1, 'b':1, 'c': 1}
# 5th loop:
    # d = {'a': 1, 'x': 1, 'b':1, 'c':1}
    # d.setdefault('c', 0) + 1 = 1 + 1 = 2
    # d = {'a': 1, 'x': 1, 'b':1, 'c': 2}

d = dict(a = 1)
dd = defaultdict(a = 1)

print(d == dd) # True

classes = ['math', 'english']
students = ['John', 'Alice', 'Bob']

# dict = {'math': ['John', 'Alice', 'Bob'], 'english' = ['John', 'Alice', 'Bob']}

# dd = defaultdict(list)
# for c in classes:
#     dd[c].extend(students)
# print(dict(dd))



def f(t):
    return t[0]

d = {'x': 3, 'b': 1, 'a': 2, 'f': 1}
print(d.items())
for key, value in sorted(d.items(), key = (lambda t: t[0])):
    print(key, '->', value)
print('--------------------')
for key, value in sorted(d.items()):
    print(key, '->', value)
print('--------------------')
print(d.keys())

for key in sorted(d.keys(), key = (lambda k: k)):
    print(key, '->', d[key])


# f = lambda x, y: x+y
# print(f(1, 2))
# print((lambda x, y: x+y)(1, 2))


for key in sorted(d):
    print(key, '->', d[key])

# 2
print('--------------------')
for key, value in sorted(d.items(), key = (lambda t: t[1])):
    print(key, '->', value)
# b -> 1
# f -> 1
# a -> 2
# x -> 3


print(dir())



