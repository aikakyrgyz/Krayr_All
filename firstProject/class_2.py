
# Data types:
# Numbers: Integers and Floats, ex: int = 4; float = 2.5
# bool
# Strings: Ex: 'string'
# Variables: age = 20
# basic functions: print, input, type
# We use == signs for comparison, e.g. 2 == 3 -> False
# but one = sign for assignment, e.g. name = 'John'

# Boolean Operators:
# and: &
# or: |
# not: !=

# new line character
age = 10

print(type(age)) # class <int>

name = "John"
print(type(name)) # class <str>

float = 10.5

print(type(float)) # class <float>



# Relational operators: =, <, >, <=, >=, !=


country = 'Poland' # assigning the value

# chaining relational operator
x = 3
print(0 < x < 5)

yes = True
no = False

print(type(yes)) # <class 'bool'>
print(type(no)) # <class 'bool'>

print(type(2 > 3)) # print(type(False)) #<class 'bool'>

print(type(True))

country2 = "Germany"

print(country == country2) # False


drivers_license = True
age = 19


a = -2
b = 0
print(a >= 0 and b <=0) # (False and True) -> False
# short-circuit evaluation

a = 9
b = 10

print(a == 10 and b == 0) #(False-> False)

c = 0

print( a == 9 and b == 10 and c < -2)  # (True and True and False) -> False

country = 'Poland'
continent = 'Europe'
verb_to_be = ' is '

print(10, 20, sep = '/') # argument here is the '/', sep = separator

print(country, continent, verb_to_be, sep = '...')

print(country, continent, sep = verb_to_be)
print(country, continent, sep = ' is ')

sentence = 'This is some sentence\n\n\n'
print(sentence) # already has a new line implemented

print(country, continent, sep = verb_to_be, end = '.\n\n') # end it with the .


x = 5
y = 7
z = 10
print(x, y, sep = '/', end = '') # 5/7
print('\n') # inside quotation marks
print('\t') # tab

print('Countries:\n\tTurkey,\n\tGermany,\n\tItaly\n')
# first way, replace single quotation mark with double "
print("It's a beautiful day")
# second way
print('It\'s a beautiful day')


print() # print a new line

print(x, y, sep = ' ') # 5 7

print(x + y + z) # 22

# built-in function: input

# age = input() #18
# bar

# type casting
print(type('2')) # class <str>
number = int('2')
print(type(number)) # class <int>

number = 10
print(str(number)) # class <str>

print("Bar")

# age = int(input()) # int('18')

# Remember that: input() returns a strings

# age = int(input("Please enter your age: ")) #prompt # 20

# age is still a string
# age = input("Please enter your age: ")
# print(type(age))
# command + '/'

# the last value that it was bounded to is saved
# driver_license = bool(input("Do you have a driver's license?"))
# print(driver_license)
# print(type(driver_license))
# True: Yes
# False: No


# driver_license: separated two words by an underscore

# PEP8: guidelines for writing code

# ClassName

# built-in method len() only works for strings, not for int
word = 'raspberry'
# how many letters in this word

print(len(word)) # 9
print(len('raspberry')) # 9

word = 'raspberry\n'
print(len(word)) # 10

print(len('a 2')) # 3 # also counts the space

print(len('a//b')) # 4
# does not mean: print(a//b)

# print(len(5)) # TypeError

print("one" + ' and ' + 'two')
# print("one" + 1) # TypeError: can only concatenate str (not "int") to str

# print(3;) # Syntax Error
# print(non_existent_variable) # NameError: name 'non_existent_variable' is not defined

word = 'YEY '
print(word * 100)


# Relational Operators on Strings

name = 'Johny'
name2 = 'John'

print(name == name2) # False
print('Johny' == 'John')

print(name != name2) # True

print('John' == 'john') # False

# Python ASCII
# Dictionary
# Apple
# Bubble
# Word

# String methods

# .strip()
# syntax: string.strip()
# what it does: strip the whitespace from both sides
# whitespace: ' ', '\n', '\t'
# not strip(string)

description = '                         Okay, here we have redundant whitespace on both sides                   '
print(description)
description = description.strip()
print(description)

# .upper()

word = 'congrats'
word = word.upper()
# 'congrats'.upper()
print(word) # CONGRATS

# .lower()

word = 'CONGRATS'
print(word.lower())

# .isupper()
# whenever you have an is within the method name, it means that it return a bool

word = 'CONGRATS'
print(word.isupper()) # True

word = 'congrats'
print(word.isupper()) # False

# .islower()

print('CONGRATS'.lower().isupper()) # False
# 1. 'CONGRATS'.lower() -> 'congrats'
# 2. 'congrats'.isupper() -> False

print("yey".lower().upper().isupper()) #True
# 1. 'yey'.lower() -> 'yey'
# 2. 'yey'.upper() -> 'YEY'
# 3. 'YEY'.isupper() -> True

# .startswith(arg)
# what it does: returns a bool, whether or not the string starts with the specified argument

word = 'Bottle'
print(word.startswith('B')) # True

print('One day'.startswith('One')) #True

value_returned = word.startswith('B')

print('The value started with B:', value_returned, '\nAnd the type of the returned value is ', type(value_returned)) # The value started with B: True

length = len('raspberry')
print(len('raspberry'))
print(length)

word = '        '
print(word.startswith(' '))

word = '         sentence     '
print(word.strip().startswith(' ')) # false

print(word.strip().startswith('s')) # true

# .title : capitalizes the word
capital = 'paris'
print(capital.title())

# .rstrip(); lstrip()
word = '         on the left'
print(word.lstrip())
word = 'on the right               '
print(word.rstrip(), end = '.')

# .replace()
print()
word = 'bed'
print(word.replace('e', 'a'))


name  = 'John'
age = 18


print('The name is ', name, 'and the age is: ', age )

# f'string

print(f'The name is {name} and the age is: {age}') #The name is John and the age is: 18


# you can also evaluate expressions within the braces
capital = 'paris'
country = 'france'
print(f'The capital of {country.title()} is {capital.title()}')
print(f'The product of number 111*222 is {111*222}')

print(f'The type of True is {type(True)}') #print(f'The type of True is {type(True)}')





