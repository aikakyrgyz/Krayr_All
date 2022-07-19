
# Modules are a namespace -- a place where names are created. And names that live in a module are called attributes.
# Technically, modules correspond to files, and Python creates a module object to contain all the names defined in the file
'''
How do files become namespaces? Everyname that is assigned a value at the top level of a module file (i.e. not in a
function body) becomes an attribute of that module. For instance, fiven an assignment statement such as x = 1 at the top
level of a module file myModule.py, the name x becomes an attribute of myModule which we can refer
to from outside the module as myModule.x   . The name x also becomes a global variable to other code inside myModule.py
'''

'''
Classes

Classes are mostly just a namespace, much like modules. But unlike modules, classes also have support for multiple copies, 
namespace inheritance, and operator overloading. 

What is OOP? Object-oriented programming, it is programming technique that relied on the concept of classes and objects,
rather than functions and logic. 

There are two kinds of objects in Python's OOP model:
1. class objects
2. instance objects

Class objects provide default behavior and serve as generators for instance objects.
Instance objects are the real objects your programs process, each is a namespace in its own right, but inherits (i.e. has
access to ) names in the class it was created from. 

So, each time you call a class, you get a new instance. 

Inside class methods functions, the first argument (called "self") references the instance object being processed, 
assignments to attributes of "self" create or change data in the instance, not the class. 



types of variables

1. local variables
2. instance variables
3. class variables
4. global variables

Class variables: they "live" inside the class definition, so there is one copy shared by all instances of the class.

Instance variables: vary among different class objects, but are the same type for all. 

'''


class Lego:

    for_all = 0 # class variable
    def __init__(self):
        self._elements = [] # instance variable

    def add(self, new_elements: list):
        # self._elements.extend(new_elements)
        self._elements += new_elements

    def size(self):
        return len(self._elements)

    def get_elements(self):
        return self._elements

    def __len__(self):
        '''Always returns an integer'''
        return len(self._elements)

    def __add__(self, other):
        '''Returns a new object created from combining the two'''
        new_toy = Lego()
        new_toy._elements = self._elements + other._elements
        return new_toy

    def __eq__(self, other):
        '''Returns bool'''
        return self._elements == other._elements

    def __str__(self):
        '''Always returns a string'''
        return str(self._elements)



print(type(Lego)) # <class 'type'>
print(type(Lego.__init__), type(Lego.add), type(Lego.size))

# creating an instance object
toy1 = Lego()
print(type(toy1))
print(type(toy1.add))
toy2 = Lego()

print(toy1 is toy2) # False

# toy1.x = 6
# print(toy1.x)
print(toy1._elements)

toy1.add([1, 2, 3])
toy2.add([100])

print(toy1._elements)
print(toy1.for_all)

print(toy2._elements)
print(toy2.for_all)

print(toy1) # <__main__.Lego object at 0x7fb2cc238be0>

print(len(toy1))

print('----------- DUNDER METHODS ----------------')

toy1 = Lego()
toy2 = Lego()
toy1.add([1, 2])
toy2.add([1, 2])

# using __add__
toy3 = toy1 + toy2


print('The elements of toy3 are', toy3.get_elements())

print(toy3.size())

print('The value of toy3 is', toy3)

# using __len__
print('The length of toy3 is', len(toy3))

print(toy1 == toy2)



class Int_set(object):
    ''' An Int_set is a set of integers'''

    def __init__(self):
        self._vals = []
        # [1 ,2, 4 ]

    def insert(self, element):
        if element not in self._vals:
            self._vals.append(element)

    def member(self, element):
        return element in self._vals

    def remove(self, element):
        try:
            self._vals.remove(element)
        except:
            raise ValueError(str(element) + ' not found')

    def get_members(self):
        return self._vals

    def __str__(self):
        if self._vals == []:
            return '{}'
        self._vals.sort()
        result = ''
        for element in self._vals:
            result = result + str(element) + ','
        return f'{{{result[:-1]}}}'


    def union(self, other):
        '''Assuming other is an object of the type Int_set'''
        # self._vals.extend(other.get_members())
        for element in other.get_members():
            self.insert(element)

# create an instance object
s = Int_set()
s.insert(5)
# print(s._vals)
print(s.get_members())
print(s.member(5))
print(s.member(10))
s.remove(5)
s.insert(20)
s.insert(100)
print(s.get_members())
print(s)
print(str(s))

##################

j = Int_set()
print(j)
j.insert(20)
j.insert(30)
# s.remove(100)
print(j.get_members())
print(s.get_members())

# -> s._values = [20, 30, 10, 100]
s.union(j)
print(s.get_members())



# Magic Methods/Dunder methods
# dunder -> double underscore



'''
+: __add__
-: __sub__
*: __mul__
//: __floordiv__
/: __truediv__
%: __mod__
**: __pow__ 
==: __eq__
!=: __neq__
<=: __le__
>=: __ge__
<: __lt__
>: __gt__
'''













