
##################### Lambdas  #####################

# Lambda: is an expression that generates function objects

# Syntax: lambda arg1, arg2, ... , argN: expression using arguments

# Lambda always returns some value

# Why use lambdas? Lambdas can be included in places where you would be not able to define a function (def ...).

# We can only have one line, not a block of statements

def f(x, y):
    return x+y


print(f(5, 5))
f = lambda x, y: x+y
print(f(5, 5)) # 10

print((lambda x, y: x+y)(5, 5))

f = lambda x, y, c, d: x*y+c+d
print(f(1, 2, 3, 4))


# frozenset = a set that is immutable
# s = frozenset({1,2,3})
# print(s)


####################### SORTING ###################


# Both by default sort in ascending order (-> increasing order ->)
# 1. sort: is a method that is defined for LISTS only. It returns None and mutates the list in place. No need to
# reassign the value and save the sorted list.

# 2. sorted: is a function that can be used on any iterable data types -> lists, tuples, dict, sets, frozenset.
    # sorted does not mutate the iterable. It creates a copy of the iterable, sorts it and returns it as a list, but does not
    # mutate the original iterable

l = [6, 9, 10, 12, 1]
l.sort()
print(l) # [1, 6, 9, 10, 12]


l = [6, 9, 10, 12, 1]
print(sorted(l)) # l = [6, 9, 10, 12, 1]
print(l) # [6, 9, 10, 12, 1]

s = {1, 7, 3, 100}
print(sorted(s)) # [1, 3, 7, 100]
print(s)

t = (30, 60, 10, 50)
print(sorted(t))  # [10, 30, 50, 60]


country = [('Poland', 30), ('Mexico', 100), ('Italy', 10), ('Sweden', 20), ('Australia', 90)]
# country.sort()
print(country)




# x, y = (4, 5)
# print(x) # 4
# print(y) # 5

# for country, index in country:
#     print(f'Country: {country} with the index {index}')

for c, index in sorted(country): # for c, index in [('Australia', 90), ('Italy', 10), ('Mexico', 100), ('Poland', 30), ('Sweden', 20)]
    print(f'Country: {c} with the index {index}')
print(country)


# def sorted(iterable):
#     copy = list(iterable)
#     copy.sort()
#     return copy

for num in sorted((1, 100, 44, 99, -4, -10, 0)):
    print(num)


l = [1, 99, 0, 55]
l.sort(reverse=True) # descending order
print(l) # [99, 55, 1, 0]


################## NOTE! #########################
# country = [('Poland', 30), ('Mexico', 100), ('Italy', 10), ('Sweden', 20), ('Australia', 90)]
# for c, index in country.sort():
#     print(f'Country: {c} with the index {index}')
# print(country)
############################################

country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Australia': 90}
print(country)

# country.sort() -> AttributeError because the .sort() method only works for lists


# sorts by key
print(sorted(country)) # ['Australia', 'Italy', 'Mexico', 'Poland', 'Sweden']
country_sorted = sorted(country)
print(country)

print(sorted(country, reverse = True)) # ['Sweden', 'Poland', 'Mexico', 'Italy', 'Australia']

# sort each tuple

print(sorted(country.items())) # [('Australia', 90), ('Italy', 10), ('Mexico', 100), ('Poland', 30), ('Sweden', 20)]


##### print dictionary ########

country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Australia': 90}
for c in sorted(country): # for c in ['Australia', 'Italy', 'Mexico', 'Poland', 'Sweden']
    print(f'Country: {c} and the index is: {country[c]}') # country['Australia']
print(country)

####################################

country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Australia': 90}
for c, index in sorted(country.items()):
    print(f'Country: {c} and the index is: {index}')

#################################
country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Australia': 90}
for c, index in sorted(country.items(), reverse = True):
    print(f'Country: {c} and the index is: {index}')

country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Australia': 90}
country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Australia': 90}
print(list(country.items()))  # [('Poland', 30), ('Mexico', 100), ('Italy', 10), ('Sweden', 20), ('Australia', 90)]
print(sorted(country.items())) # [('Australia', 90), ('Italy', 10), ('Mexico', 100), ('Poland', 30), ('Sweden', 20)]

#################################
country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Australia': 90}
country = list(country.items())
country.sort()
print(country)
################################
# syntax: sorted(country, reverse=True)


####################### HOW DOES PYTHON COMPARE AND SORT #####################
 # ASCII value of a character, use ord
print(ord('a'))
print(ord('A'))
print('A' < 'a') #-> True
print('apple' < 'android') # -> False
print('apple' < 'apple1') # -> True -> len('apple') < len('apple1')
print('apple' < 'apple ') # -> True -> len('apple') < len('apple ')

# all digits < all upper_case letters < all lower_case letters

print('TINY' < 'big') # True

print('TINY'.lower() < 'big') # False


print('5'<'15') # False

print('dog'< 'da') # False

################# COMPARE TUPLES ###################
print(('JUNE', 30) < ('JULY', 31)) # False

print(('JUNE', 30) < ('JUNE', 31)) # True

print(('JUNE', 31, 'extra') < ('JUNE', 31)) # False len(tuple1) < len(tuple2)

#################################
# dictinary unique values

country = (('Poland', 10), ('Poland', -10), ('Poland', 20), ('Poland', 100), ('Poland', 0), ('Poland', 100, 'extra'))
print(country)
print(sorted(country))

##########################
 # Sort by index of that country

def country_index(t):
    return t[1]

country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Australia': 90}
for c, index in sorted(country.items(), key = country_index, reverse = True): # key = country_index(('Poland', 30))
    print(f'Country: {c} and the index is: {index}')
print(country.items())  # [('Poland', 30), ('Mexico', 100), ('Italy', 10), ('Sweden', 20), ('Australia', 90)]
'''
Country: Italy and the index is: 10
Country: Sweden and the index is: 20
Country: Poland and the index is: 30
Country: Australia and the index is: 90
Country: Mexico and the index is: 100
'''
print(sorted(country.items(), key = country_index)) # [('Italy', 10), ('Sweden', 20), ('Poland', 30), ('Australia', 90), ('Mexico', 100)]


####### use lambda instead of declaring a function

country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Australia': 90}
for c, index in sorted(country.items(), key = lambda t: t[1]): # key = country_index(('Poland', 30))
    print(f'Country: {c} and the index is: {index}')
print(country.items())  # [('Poland', 30), ('Mexico', 100), ('Italy', 10), ('Sweden', 20), ('Australia', 90)]

####################################
# sort in descending order, instead of using reverse, note only works for numeric values
country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Australia': 90}
for c, index in sorted(country.items(), key = lambda t: -t[1]): # key = country_index(('Poland', 30))
    print(f'Country: {c} and the index is: {index}')
print(country.items())  # [('Poland', 30), ('Mexico', 100), ('Italy', 10), ('Sweden', 20), ('Australia', 90)]

#########################

# Sort by the value (most prioritized) then by the key
country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Germany': 90, 'Australia': 90}
for c, index in sorted(country.items(), key = lambda t: (t[1], t[0])): # key = country_index(('Poland', 30))
    print(f'Country: {c} and the index is: {index}')
print(country.items())  # [('Poland', 30), ('Mexico', 100), ('Italy', 10), ('Sweden', 20), ('Australia', 90)]

#######################
country = {'Poland': 30, 'Mexico': 100, 'Italy': 10, 'Sweden': 20, 'Germany': 90, 'Australia': 90}

# can pass items, keys, and values to the dictionary
print(sorted(country.items()))
print(sorted(country.values()))
print(sorted(country.keys())) # < == > sorted(country)

# sort by the value of the dictionary
print(sorted(country.items(), key = (lambda t: t[1])))
# sort in descending order (<- decreasing order <-)
print(sorted(country.values(), key = (lambda t: -t)))


# if you want to save the sorted list then:

my_sorted_db = sorted(country.items(), key = (lambda t: t[1]))
print(my_sorted_db)

#######################

a = [[0], [1], [2]]
b = list(a)

a[0][0] = 'C'
print(a, b)
b.append([3])
print(a)
print(b)

########
#
'''
Given a list of groceries in the format (Name, Price, BestByDate) sort them in the order as specified: 
groceries = [('Milk', 30, (6, 3, 2022)), ('Bread', 10, (6, 6, 2022)), ('Salad', 5, (6, 6, 2022)), ('Corn', 60, (12, 31, 2023)), ('Chocolate', 100, (7, 4, 2022)), ('Candy', 100, (7, 4, 2022))]

1. In the alphabetical order of the name of the produce
2. In the increasing order of the price, so that the produce with the lower price appears before the one with the higher price
3. In the decreasing order of the price, so that the produce with the higher price appears before the one with the lower price
4. In the increasing date order, so that the produce that is expiring earlier appears the first in the list. 
5. In the increasing year order, so that the produce with the lower expiring YEAR appear before the higher year values
6. In such order so that the produce that should be sold first appears earlier in the list and so that the alphabetical order
of the names is preserved, i.e. Candy appears before Chocolate.

  
groceries = [('Milk', 30, (6, 3, 2022)), ('Bread', 10, (6, 6, 2022)), ('Salad', 5, (6, 6, 2022)), ('Corn', 60, (12, 31, 2023)), ('Chocolate', 100, (7, 4, 2022)), ('Candy', 100, (7, 4, 2022))]
groceries.sort(key = lambda t: t[1])
print(groceries)
groceries.sort(key  = lambda t: t[2])
print(groceries)
groceries.sort(key = lambda t: (t[2], t[1]))
print(groceries)
'''
groceries = [('Milk', 30, (6, 3, 2022)), ('Bread', 10, (6, 6, 2022)), ('Salad', 5, (6, 6, 2022)), ('Corn', 60, (12, 31, 2023)), ('Chocolate', 100, (7, 4, 2022)), ('Candy', 100, (7, 4, 2022))]
print(groceries)