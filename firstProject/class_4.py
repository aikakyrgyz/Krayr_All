
import math
# pow
# root()
# abs()
# floor()


# some more string methods

# replace()
# old - old substring you want to replace
# new - new substring which will replace the old substring
# count (optional) - the number of times you want to replace the old substring with the new substring
# If count is not specified, the replace() method replaces all occurrences of the old substring with the new substring.
"""
# substring is just a piece of a string
string = 'apple my today apple'
string = string.replace('apple', 'banana', 1 )
print(string)

string = 'Paris'
string.replace('P', 's') # saris

# index()
# returns the (first) index of the found substring
# raises an Error if the substring is not found
string = 'Paris'
print(string.index('s')) #4

# print(string.index('w')) # ValueError: substring not found

# find()
# same as index, but does not raise an error, just returns -1

string = 'Paris'
print(string.find('a')) # 1
print(string.find('w')) # -1 (does not raise an error)

# isalnum()
# are all characters alphanumeric
string = 'country12343'
print(string.isalnum()) #True
string = 'he$llo!'
print(string.isalnum()) #False

# isdigit()

string = 'a'
print(string.isdigit()) # False
string = '125'
print(string.isdigit()) # True

# are all digits

# isalpha
# are all letters
string = 'onlylettershere'
print(string.isalpha()) # True
string = 'only letter and a number: 1'
print(string.isalpha()) # False


# Note: whitespace is not counted as alphabetic


# count(value, start, end)
string = 'apple'
print(string.count('a')) # 1
string = 'apple and'
print(string.count('a')) # 2

string = 'apple and'
print(string.count('a', 0, 5)) # 1

# split()
# splits the string and returns it as a list
# default separator: whitespace

string = 'today tomorrow yesterday'
print(string.split()) #['today', 'tomorrow', 'yesterday']

string = 'today,tomorrow,yesterday'
print(string.split(',')) # ['today', 'tomorrow', 'yesterday']

string = 'apple|banana|fruit'
print(string.split('|')) # ['apple', 'banana', 'fruit']

############################ FUNCTIONS ####################
# the reasons:
# hides the complexity: abstraction
# you want your code to be modular
# easier to find bugs

# writing functions

# type annotation
# def function_name() -> int:
#     #code ...

# define a function
# SYNTAX:

def name_of_the_function():
    # write your code here
    return


# built-ins

def replace():
    # some code that takes care of string replacement
    return 'some string'

# Remember: every function in Python (both built-in and your own) return some value
# the type of the value can be anything, int, or str, or float, list, None

# Note: defining and calling are two different things


def give_10():
    return 10


print(give_10()) # 10

number = give_10()
print(number) # 10

print(give_10() + give_10()*10) #110
    # 10 + 10*10 = 110

print(give_10) # <function give_10 at 0x7fa6c7a3a790>

print(type(give_10)) # <class 'function'>

# functions with defined parameters

# square_number(5) # -> 25

def square_number(num):
    square = num * num
    return square




square_of_it = square_number(5)
print(square_number(5)) # 25
print(square_of_it)
print(square_of_it + 5) # 30

def square_number(num):
    print('This is printed', num*num)

square_number(5)



def square_number(num):
    return num * num # returned an int

# Difference between a parameter and an argument

# in this function:
'''
def square_number(num):
    return num * num # returned an int
'''
# parameter: num (when you define the function)
# parameter is what the function is expecting
# argument: when you call it

# square_number(5)

# argument is 5
# argument is what is actually being passed


###########################
def triple_number(num):
    return num*num*num

triple = triple_number(3)
print(triple) #27

################

# Docstrings

def triple_number(num):
    'Return a triple of a number' # one-line docstring
    return num*num*num

def triple_number(num):
    '''
    Calculates a triple
    Adds a five to the triple
    '''
    triple = num * num * num
    return triple + 5



################################

def triple_uses_square_function(num):
    ' Uses the square function'
    return square_number(num) * num

print(triple_uses_square_function(5)) # 125


################################

#
# def square(num):
#     return num*num
#
# def triple(num):
#     return math.pow(num, 3) # num^3
#
# def absolute(num):
#     return abs(num)
#
# def get_input():
#     return int(input("Enter any number: "))
#
#
#
# number_enter = get_input()
# print('The square is: ', square(number_enter))
# print('The triple is: ', triple(number_enter))
# print('The absolute value: ', absolute(number_enter))

###############################


# Online Python - IDE, Editor, Compiler, Interpreter

# Scope and Scoping Rules


# each data piece within python has its own scope  (house that it resides)
x = 5


def read_cc():
    while True:
        city = input('What is your city? ')
        if city == '':
            print('Please enter the city')
        else:
            country = input('What is your country?')
            if country == '':
                print('Please enter the country')
            else:
                return 'You are in ' + city + ", " + country
    print(locals())


# print('Calling the function')
# string = read_cc()
# print(string)
# print('--------------')
# # print(city) # raises NameError, it is not defined in the global scope
# print(x)
# Variables inside your function are only local to that function
# Local: they only exist and accessed within that the scope
# Global: read__cc
print(globals())

x = 10
y = 15
z = 20


def function(a, b, c):
    # a, b, and c are considered local
    sum = a + b + c
    return x + y + z + sum


print(function(1, 1, 1))  # 48

#############################


x = 15


def function(num):
    x = num + num  # brand new x , that is only local to this function
    return x


print(function(x))  # 30
print(x)  # 15

#######################################

# x = 5
#
# def function(num):
#     m = x * num
#     x = m * num
#     return x # returns an Error, local variable 'x' referenced before assignment
#
#
# print(function(x))
# print(x)


##################################################
# In python, your variable within the function must be either local or global

# whenever a function is entered, first Python scans the what kind of local variables it has


x = 5
def function(num):
    global x
    m = x * num
    x = m * num
    return x # 125


print(function(x))
print(x)
##################################################

x = 1 # global


def f():
    x = 2 #local to function f
    print(x)

f()       # 2

print(x)  # 1

# Rule: When Python exits the function, the local varibales within it are destroyed
    # : local variables of the function exist only during the function's life cycle

################################################

x = 1

def f():
    w = 2
    print(x, w)


f()      # 1, 2
print(x)  # 1
# print(w) #  name 'w' is not defined

####################################

# x = 1
# def f():
#     y = 2
#     print(x, y) #  UnboundLocalError: local variable 'x' referenced before assignment
#     x = 2
#
# f()
# print(x)
# # The problem here is that x is being both local and a global, but it can only be either local or global within the function


###################################


x = 1
def f():
    y = 2
    x = 2
    print(x, y)

f() # 2 2
print(x) # 1

#################################


x = 1

def f():
    global x
    y = 2
    print(x, y)
    x = 2 # global, rebind the value of x

f() # 1 2
print(x) # 2

#######################

x = 1

def f():
    y = 2
    print(y)
    x = 2 # local, the global variable is not touched

f() # 2
print(x) # 1


#########################



def f():
    global x
    x = 2
    y = 2
    print(x, y)

f() # 2 2
print(x) # 2

############################
total = 0
x = 3
def read_and_calculate_sum():
    def read_number():
        return int(input('Enter a number, or -1 to end the program: '))
        

    total = 0

    while True:
        number = read_number()
        if number == -1:
            return total # break

        total += number


print(read_and_calculate_sum())

"""


# Scope Look Up for variables and methods: Local, Enclosing, Global, Built-in (LEGB)

# First, check the local scope
# If the variable name is not found in the local scope, it looks at the enclosing # somewhere between the local and the global
# If the variable name is not found in the enclosing scope, it looks for it in global scope 
# If the variable name is not found in the global scope, it looks it up in the built-ins

def f():
    x = 5 # in enclosing scope
    def f1():
        print(x)
        
        
#################################


# Function that returns a function
def age_is_bigger(age):
    # print(locals()) # {'age': 18}
    def f(x):
        return x > age
    return f

# 25 > 18
# 45 > 18

# 45 > 21
# 23 > 21

old_enough = age_is_bigger(18) # old_enough = x
print(old_enough(25)) # f(25)  # 25 > 18
# True

old_enough = age_is_bigger(21)
print(old_enough(25)) # # 25 > 21 # True












