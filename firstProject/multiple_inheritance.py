

class C:
    pass	   # object is the base class of the derived class C


class B(C):	   # C is the base class of the derived class B
    x = 100
    def say_hello(self):
        print('Hello! From B')


class D: # object is the base class of derived class D
    x = 10
    def say_hello(self):
        print('Hello! From D')




class A(B,D): # B and C (in that order) are the base classes of A
    def method_a(self):
        print('Method in A')

    def access_attribute(self):
        print(super().x)


a = A()
a.method_a()
a.access_attribute()
a.say_hello()

print(a.__dict__)
print(A.__dict__)

##############
# class A(object):
#     pass
#
# class B(object):
#     pass
#
# class C(A, B):
#     pass
#
# class D(B, A):
#     pass
#
# class E(C, D):
#     pass

# print('E mro:', E.mro())

"""
Search of an attribute/method in multiple inheritance:

(a) Python first tries to find the attribute in the instance object.

(b) If Python fails, it searches the class that it was constructed from.

(c) If Python fails, it searches (LEFT before RIGHT) upward from the class the
    object was constructed from (which appears at the bottom of the network),
    towards the root/object class.

(d) If Python reaches any base class and has not already searched all of its
    derived classes, that base class is not searched now; instead the derived
    class searches its REMAINING (to the RIGHT) base classes; and if it has
    searched all its base classes, its derived class searches its remaining (to
    the right) base classes, etc. 
    So, a base class can be searched ONLY if ALL its derived classes have already been searched.
"""

# How does Python know about the parent class(es) of a class.
# Every class object has a __bases__ attribute that is a tuple of its base
# classes; the order that it uses for the base classes in the tuple is the same
# order the base classes appear in the class definition.


print("A's base classes", A.__bases__)
print("D's base classes", D.__bases__)

# For single-inheritance all of the classes would only have one base

''' 
But How Python Actually Searches for Attributes:
The order of classes that Python uses to search for an attribute name is
actually computed when a class is defined (so the order doesn't need to be
recomputed for each attribute access); it is stored in the class attribute
__mro__

MRO: Method Resolution Order
but it is not only related to methods but also for attributes.

'''

print("A's mro", A.__mro__)
print("D's mro", D.__mro__)
print(D.mro())
print("B's mro", B.mro())

"""
If there is no order that satisfies all these requirements (see below for an
example) then the algorithm will detect this fact and Python will raise a
TypeError exception when the class itself is defined: the __mro__ attribute for
the class is computed when the class is defined. The result of raising the
TypeError is that the class will not be defined and cannot be used.
"""

# isinstance method

a = A()
print(isinstance(a, A))

print(isinstance(10, int))

print(isinstance(10, list))

# what if did isinstance(a, D), even though we created the object a from A class

print(isinstance(a, D))

# It prints True, so isinstance returns true as long as it was inherited from that class,
# not necessarily directly created from that class.

# so it is the same as saying
print(D in type(a).__mro__) # since D is included in the __mro__ of A
# and if we would search for some attribute a.x, then it would first try to search
# the instance object a itself, then it would not find it there,
# search in B, then in C, then finally in D (let's say the x is defined in D), then it would stop

print(issubclass(A, D))
print(issubclass(A, object))
print(issubclass(D, B))


# Exception and Inheritance

'''
All exceptions are arranged in an inheritance hierarchy.
If we wrote ->
try:
    ...
except SomeError:
    ...

This fragment would handle a raised exception that is from the SomeError class
or any class DERIVED from it (i.e. any handles any exception object o
for which isinstance(o, SomeError) is TRUE
'''

# Code from GeeksforGeeks website: prints the hierarchy of all exceptions in Python
#
# # import inspect module
# import inspect
#
#
# # our treeClass function
# def treeClass(cls, ind=0):
#     # print name of the class
#     print('-' * ind, cls.__name__)
#
#     # iterating through subclasses
#     for i in cls.__subclasses__():
#         treeClass(i, ind + 3)
#
#
# print("Hierarchy for Built-in exceptions is : ")
#
# # inspect.getmro() Return a tuple
# # of class  cls’s base classes.
#
# # building a tree hierarchy
# inspect.getclasstree(inspect.getmro(BaseException))
#
# # function call
# treeClass(BaseException)




# let's look at the ArithmeticError
# ------ ArithmeticError
# --------- FloatingPointError
# --------- OverflowError
# --------- ZeroDivisionError

# print(10/0)
try:
    print(10/0)
except ZeroDivisionError:
    print('Cannot divide by zero')

# but what if we did
try:
    print(10/0)
except ArithmeticError as e:
    print(e)
    print(type(e))
    print(isinstance(e, ArithmeticError))
    print('Cannot divide by zero')

# so, it would still catch it, why ??? because ZeroDivisionError
# is the derived class of the ArithmeticError, so the ZeroDivisionError is an ArithmeticError

# and if we had:
try:
    print(10/0)
except ArithmeticError:
    print('Arithmetic Error')
except ZeroDivisionError: # never going to reach this block
    print('ZeroDivisionError')



# let's look at the OS Error in particular

#
# class BaseException(object):
#     pass
#
# class Exception(BaseException):
#     pass
#
# class OSError(Exception):
#     pass
#
# class ConnectionError(OSError):
#     pass
#
# class BrokenPipeError(ConnectionError):
#     pass
#
# class FileNotFoundError(OSError):
#     pass
#
# print(issubclass(FileNotFoundError, BaseException))
#
# print(FileNotFoundError.mro())
# print(BrokenPipeError.mro())



# If we wrote:

# 1. except BrokenPipeError: handles only the BrokenPipeError, since it is not the parent class of any child class
# 2. except ConnectionError: handles both ConnectionError and BrokenPipeError
# 3. except OSError: handles OSError, ConnectionError, FileNotFoundError, and BrokenPipeError
# 4. except Exception: handles Exception, OSError, ConnectionError, FileNotFoundError, and BrokenPipeError
# ... so on
#
# # note you can also write the Exception classes in a tuple:
# # except (ConnectionError, BrokenPipeError)
# # can be any number of classes in the tuple
#
# # So be careful when trying to catch exceptions that have a base class that is also one of your except lines.
#
#
# # Encapsulation: bundling together of data attributes and methods for operating on them.
#     # putting things in common together.
#



# # Information Hiding
#     # Making the attributes private, so that the users of the class can access the data only
#     # only through the object's methods.
#     # There is not keyword to make attributes private, but Python3 offers a mechanism to make
#     # attributes invisible invisible outside the class. Put the double underscores __ in the
#     # beginning of the attribute's name and not at the end.
# #


class HideInfo(object):

   def __init__(self):
       self.visible = 'I am visible!'
       self._visible = 'I am also visible, but you should not access me directly'
       self.__visible__ = 'Don\'t get tricked! I am also visible'
       self.__invisible = 'I am invisible from outside!'

   def print_visible(self):
       print(self.visible)

   def print_invisible(self):
       print(self.__invisible)

   def __print_invisible(self):
       print(self.__invisible)

   def __print_invisible__(self):
       print(self.__invisible)


i = HideInfo()
print(i.visible)
print(i._visible)
print(i.__visible__)
# print(i.__invisible) # raises an AttributeError
#
# ######## __ can also be put in front of method names
# #
i = HideInfo()
i.print_visible()
i.__print_invisible__()
# i.__print_invisible() # raises an AttributeError

#
# ## now let's create a child class for HideInfo
# #

class HideInfoChild(HideInfo):
   def child_print_invisible(self):
       print(self.__invisible)


# #
# c = HideInfoChild()
# c.child_print_invisible() # AttributeError, but in reality it makes things harder
# ## since we would want the Child class to still be able to access the private attribute of the Parent class
# ## but using __ does not allow us to do it. So , programmers usually do not take the advantage of the __ information
# ## hiding technique.
# #
#
#


# ######## MIXINS ###########
# # 1. What are Mixins? Mixins are small classes (that you create) that have methods and attrubutes  in order to provide an additional functionality to another class. So mixins customize and enhance another class. To use the mixin as somethings that provides additional fetures to your code, make your code(which is your class) inherit from this MIXIN you just created.
#
# # 2. When would you want to use a mixin? In 2 cases:
#     # - In order to provide a lot of optional features for a class.
#     # - In order to use one particular feature in a lot of different classes.
#
# # 3. You usually do not create new instance objects from mixins.
#


# Mixin

class MixinforSchool:
    def clean(self):
        print('Clean school')


class MixinOpenSchool:
    def open(self):
        print('Opening at 8am')

class University(MixinforSchool, MixinOpenSchool):
    def __init__(self, name):
        self.name = name


class HighSchool(MixinforSchool):
    def __init__(self, name):
        self.name = name


class MiddleSchol(MixinforSchool):
    def __init__(self, name):
        self.name


s = University('MIT')
print(s.name)
s.clean()
s.open()
h = HighSchool('CPS')
h.clean()




# Create your own exception classes

class CapitalNameError(Exception):
    pass



class USA:
    def capital(self):
        return 'Washington'



class Poland:
    def capital(self):
        return 'warsaw'

try:
    c = Poland()
    capital = c.capital()
    if not capital.startswith('W'):
        raise CapitalNameError()
except:
    print('CapitalNameError was raised ')



class PrivacyErrorException(Exception):
    pass


# Privacy is a mixin
class Privacy:
    def __setattr__(self, attribute, value):
        print(f'Setting {attribute} = {value}')
        if attribute in self.privates:
            raise PrivacyErrorException(f'Cannot set {attribute} to a new value')
        else:
            self.__dict__[attribute] = value


class User(Privacy):
    privates = {'email', 'password'}

    def __init__(self, username, email, password):
        self.privates = set()
        self.username = username
        self.email = email
        self.password = password
        del self.privates

    # def rebind(self, email):
    #     self.email = email

my = User('APPLE', 'apple@gmail.com', 'green')
my.username = 'BERRY'
print('USERNAME', my.username)
print('EMAIL', my.email)
print('PASSWORD', my.password)

# my.email = 'berry@gmail.com' # raises an exception

# set of private attribute



# #######
# # IGNORE FOR NOW: The main differences between Mixins and Decorators are:
#
# # Decorators wrap functionality around a piece of code.
#
# # Mixins add functionality to code using Inheritance.
#
# # There are some restrictions on each method.
#
# # Mixins only work with Object-Oriented Programming and Classes.
#
# # You cannot use Mixins to modify a function or a method, only classes.
#
# # Decorators cannot add new methods or new pieces of code.
#
# # A decorator just accepts a piece of code, modifies it and returns it. It cannot add something new. If you decorate Function A, you cannot simultaneously add Function B.
#
# #
# # class GraphicalEntity:
# #     def __init__(self, pos_x, pos_y, size_x, size_y):
# #         self.pos_x = pos_x
# #         self.pos_y = pos_y
# #         self.size_x = size_x
# #         self.size_y = size_y
# #
# #
# # # class Button(GraphicalEntity):
# # #     def __init__(self, pos_x, pos_y, size_x, size_y):
# # #         super().__init__(pos_x, pos_y, size_x, size_y)
# # #         self.status = False
# # #     def toggle(self):
# # #         self.status = not self.status
# # #
# # # class LimitSizeMixin:
# # #     def __init__(self, pos_x, pos_y, size):
# # #         size_x = min(size_x, 500)
# # #         size_y = min(size_y, 400)
# # #         super().__init__(pos_x, pos_y, size_x, size_y)
# # #
# # #
# # # class LimitSizeButton(LimitSizeMixin, Button):
# # #     pass
# #
# #
# # b = LimitSizeButton(10, 20, 200, 100)
# # print(b.pos_x)
# # print(b.pos_y)
# # print(b.size_x)
# # print(b.size_y)
#
#
#
# #################### POLYMORPHISM #################
# # Polymorphism in Python is the ability of an object to take many forms. In simple words, polymorphism allows us to perform the same action in many different ways.
# # 1. Operator overloading
# # 2. Method overloading/overriding
# # 3. Inheritance
# # 4. Function polymorphism ( len function works for any type)


x = 5
z = 6

print(x + z) # x.__add__(z) -> int.__add__(x, z)

x = 'I'
z = 'am'
print(x + z) # x.__add__(z) -> str.__add__(x, z)




class Sky:
    def color(self):
        return 'blue'

class StarrySky:
    def color(self):
        return 'black'

class Cloudy:
    def color(self):
        return 'grey'

sky = Sky()
print(sky.color())

sky = Cloudy()
print(sky.color())


class Animal:
    def location(self):
        print('Whole planet')


class Fish(Animal):
    def location(self):
        print('Ocean')


class Mammal(Animal):
    def location(self):
        print('Land')


a = Animal()

a.location()

f = Fish()
f.location()

m = Mammal()
m.location()


print(len([1, 2, 3]))

print(len('123'))

print(len(dict(a=1, b=2)))
print(len({1, 2, 3}))



# Duck Typing == Polymorphism

# Duck typing is a polymorphism notion. The term duck typing is derived from a proverb that says
# everything that walks like a duck quacks like a duck, and swims like a duck is referred to like a duck
# regardless of the item. In basic terms, it indicates that if anything matches its behavior to another, it
# will be considered a member of the category to which it belongs.


# Abstract classes work as interfaces, meaning they give a hint on how the derived classes should look like

# Any classes that have at least one abstarct method is considered an abstract class

# If a class is abstract then you cannot instantiate objects from it
from abc import ABC, abstractmethod

# import abc

class Country(ABC):
    flag = True
    @abstractmethod
    def get_capital(self):
        pass

    @abstractmethod
    def get_language(self):
        pass

    def print(self):
        print('HI')


class Poland(Country):
    def get_capital(self):
        print('Warsaw')
    def get_language(self):
        print('Polish')

class USA(Country):
    def get_capital(self):
        return 'Washington'
    def get_language(self):
        print('English')

p = Poland()
p.get_capital()

u = USA()
p.get_capital()
print(u.flag)
u.print()

# c = Country()

# Inheritance


# 1. A derived/child/subclass should be just like its base class: all the base class methods should make sense for the child.
# The relationship between the child and parent class is an "IS - A" relationship.


# 2. Inheritance looks for attributes by this rule: after checking for an attribute in the namespace (__dict__)
# of an object, it is sequentially checks for it in the namespaces of each class in the __mro__ attribute.
# o = myClass()

# 3. To call a method in the parent class from the same method (that overrides it) in the child class,
# use ParentClass.method()
# class Parent():
# def __str__(self):
#   pass

# class Child():
# def __str__(self):
#     Parent.__str__()  or super().__str__()

# 4. Typically the __init__ in the child class calls the __init__ method of its parent class, passing along some arguments

# 5. A child class should not directly access the data attributes in any of its parent classes,
# instead the base class should provide methods to access/mutate it.




