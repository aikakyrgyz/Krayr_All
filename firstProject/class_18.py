
# Namespaces for objects

'''
Every object has a special variable named __dict__ that stores all its namespace bindings in a dictionary.

Writing o.a = 1 is similar to writing o.__dict__['a'] = 1; so they both associate a name with a value in the object.

The code fragment below illustraters what do we mean by the namespace:

class C:
    def __init__(self):
        pass

o = C()
o.a = 1
print(o.a) # prints 1

o.__dict__['a'] = 2
print(o.a) # prints 2

o.__dict__['b'] = 3
print(o.a) # still prints 2
print(o.b) # prints 3

So, we have seen the lower-level way to add attribute names to the namespace of an object.
Usually, we don't initialize the namespace of an object this way (which is outside of __init__),
instead we use the *automatically* called __init__ method ands its self parameter to do the initialization.



So, in reality the below two codes are equivalent:

1st code:

class C:
    def __init__(self):
        pass

o = C()
o.__dict__['x']  = 1
o.__dict__['y'] = 2
o.__dict__['z'] = 'three'
print(o.__dict__)
2nd code:

class C:
    def __init__(self, init_x, init_y, init_z):
        self.x = init_x
        self.y = init_y
        self.z = init_z

o = C(1, 2, 'three)
print(o.__dict__)


Notice: if we try to access a non-existing attribute name, let's say o.z, then an exception will be raised
But notice, it is not going to be a KeyError (which is usually raised when a key is not found in the dictionary) but rather an AttributeError
'''

class C:
    def __init__(self):
        pass

# instance object o
o = C()

o.a = 1

print(o.a) # 1

# accessing the namespace of the object o
o.__dict__['a'] = 2

print(o.a) # 2

o.__dict__['b'] = 3

print(o.b) # 3

print('The namesapce of instance object o:', o.__dict__)


############

class C:
    def __init__(self, a, b):
        self.a = a
        self.b = b


o = C(2, 3)
print(o.a)
print(o.b)
print(o.__dict__)



############## low - level ##############

'poland;germany;sweden'.split(';')

# by Python this is translated to

# type('poland;germany;sweden').split('poland;germany;sweden', ';')
'''
class str:
    # class variable
    a = 1
    def split(self, separator):
        ### code
        return splitted string
'''
# str.split('poland;germany;sweden', ';')


# object.method(...) is translated into type(object).method(object, ...) if m is not the attribute in o

# object.a is translated to type(object).a -> str.a

# accessing the namespace of the class object

class C:
    a = 10
    def __init__(self):
        pass

print(C.__dict__)

for k, v in C.__dict__.items():
    print(k, '->', v)




# assert

# in init usually we want to to ensure that a parameter is matched to an argument that stores a legal for it.
# If not, Python will raise an exception to indicate that the object being constructed cannot be constructed properly



# syntax:
# assert boolean-test: string

# equivalent to saying

# if not boolean-test:
#   raise AssertionError(string)


# let's say we want the a to be an integer and positive

class C:
    def __init__(self, a):
        # assert type(a) is int and a > 0, f'C.__init__: a -> {a} needs to be positive and of type int'
        assert type(a) is int, f'C.__init__: a -> {a} needs be an int'
        assert a > 0, f'C.__init__: a -> {a} must be positive'


        # check that a is less than 0, if it is not less than 0, then raise assertion error
        self.a = a


o = C(5)
print(o.a)

# o = C(-2) # should not allow to construct an instance object
# print(o.a)

# o = C('hello') # raises AssertionError

# o = C(-6) # raises AssertionError



class C:
    def __init__(self, word):
        assert word.startswith('a') and word[-1] == '.', f'C.__init__: the word {word} must start with a and end with a dot'


# start with an 'a' and ends with '.'
o = C('apple.')
o = C('api.')
# o = C('bubble') # raise an error



class Cat:
    # class variable, all cats have 4 paws
    paws = 4
    def __init__(self, name, owner):
        # notice that here we do not initialize paws
        self.name = name
        self.owner = owner



cat1 = Cat('Oliver', 'Bob')
print(cat1.paws)
# type(cat1).paws -> Cat.paws

cat1.paws = 3

print(cat1.paws) # instance variable

print(Cat.__dict__)
print(cat1.__dict__)

# let's say now the number of paws for cat1 is 4 again

# 1st way to change it
cat1.paws = 4


print(cat1.paws)
print(cat1.__dict__)

# 2

print(cat1.__dict__) # {'name': 'Oliver', 'owner': 'Bob', 'paws': 4}
del cat1.paws
print(cat1.__dict__) # {'name': 'Oliver', 'owner': 'Bob'}

print(cat1.paws)
print(cat1.__dict__)


d = {'a': 1, 'b': 2}
del d['a']
print(d)

cat2 = Cat('Alice', 'Aika')
print('Cat 2s paws', cat2.paws)
# type(cat2).paws -> Cat.paws

print(cat2.__dict__)
print(Cat.__dict__)


# Rule: if the attribute is not found in the instance object's namespace, then it
# is searched in the namespace of the Class object.


class Cat:
    paws = 4
    def __init__(self, name, owner, paws):
        self.name = name
        self.owner = owner
        if paws != self.paws: # type(self).paws -> Cat.paws = 4
            self.paws = paws # creating instance variable for that instance


oliver =  Cat('Oliver', 'Bob', 3)

alice = Cat('Alice', 'Aika', 4)

print(oliver.__dict__)

# {'name': 'Oliver', 'owner': 'Bob', 'paws': 3}

print(oliver.paws) # 3

print(alice.__dict__)
# {'name': 'Alice', 'owner': 'Aika'}
print(alice.paws) # 4




# Redefintion of function names (but you can redefine anything in Python)
def f():
    return 0

def g():
    return 1




# f ---> 0x100
# g ---> 0x105

f = g

# f ---> 0x105


print(f()) # 1


def f():
    return 1

f = 0

# f is not an function object anymore, it is an integer, integers cannot be called
print(f) # 0

#############################???####################################

class C:
    def __init__(self):
        print('C <<object>> is created')

# C --> 0x100 (class)
D = C

# D --> 0x100 (class)


# C --> 0x105 (function)
def C():
    print('C <<function>> is called')


x = C() # C <<function>> is called'

y = D() # C <<object>> is created

#################################################################

class C:
    def __init__(self):
        pass

x = C()
print(type(x)) # __main__.C

















