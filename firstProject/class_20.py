
# class overloading

# __getitem__(self, index)          ->: l[1], d[index]
# __setitem__(self, index, value)   ->: l[1] = 0, d[index] = value
# __delitem__(self, index)          ->: del l[1], del d[index]
# __contains__(self, item)          ->: 'x' in l


# for this MyL class, we want the indexing to start at 1 not 0

class MyL:
    def __init__(self, iterable):
        self.l = list(iterable)

    def __str__(self):
        return str(self.l)

    def __getitem__(self, index):
        print('MyL.__getitem__(...)')
        if type(index) is int:
            return self.l[MyL.change_index(index)]
        else:
            raise TypeError(f'MyL.__getitem__({index}) must be an int')


    def __setitem__(self, index, value):
        print('MyL.__setitem__(...)')
        if type(index) is int:
            self.l[MyL.change_index(index)] = value # l[0] = value
        else:
            raise TypeError(f'MyL.__setitem__({index}) must be an int')

    def __delitem__(self, index):
        print('MyL.__delitem__(...)')
        if type(index) is int:
            del self.l[MyL.change_index(index)]
        else:
            raise TypeError(f'MyL.__delitem__({index}) must be an int')

    def __contains__(self, item):
        # return item in self.l
        for i in self.l:
            if i == item:
                return True
        return False




    @staticmethod
    def change_index(index):
        return index-1 if index >= 1 else index



a = MyL(['a', 'b', 'c'])
print(a)

print(a[3]) # a.__getitem__(1) -> type(a).__getitem__(a, 1) -> MyL.__getitem__(a, 1) ->

a[1] = 'x'
print(a[1])
print(a)

# del a[1]
# print(a)

print('w' in a) # a.__contains__('w') -> type(a).__contains__(a, 'w')
print('x' in a)

# for i in a:
#     print(i)



# missing dunder method is defined for objects when it is a dictionary
# def __missing__(self, key):
#     pass



class MyD:
    def __init__(self, **kargs):
        self.d = kargs

    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            self.__missing__(key)

    def __missing__(self, key):
        print('missing called')
        self.d[key] = 0


d1 = MyD(a=1, b=2)
print(d1.d)
print(d1['a'])
print(d1['missingkey'])
print(d1.d)


# attributes

# __getattr__(self, name)               -> called when it cannot find the name attribute
# __setattr__(self, name, value)        -> sets attribute to the value
# __delattr__(self, name)               -> delete an attribute
# __getattribute__(self, name)          -> access name attribute


class My:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age

    def __getattr__(self, name):
        print('--getattr--')
        return f'Cannot find {name}'

    def __delattr__(self, name):
        print('--delattr--')
        del self.__dict__[name]

    def __setattr__(self, name, value):
        # print(f'--setattr--, setting the {name} to {value}')
        self.__dict__[name] = value


m = My('John', 20)
print(m.first_name)
print(m.age)
del m.first_name
print(m.first_name)
print(type(m))
m.a = 1
print(m.a)

# see all of the attributes in the namespace of m
print(m.__dict__)

print(m.x)
m.x = 2 # setting
print(m.x)

from collections import defaultdict

class H:
    def __init__(self):
        self.history = defaultdict(list) # __setattr__
        self.x = 0

    def increment(self):
        self.x +=1
        # self.x = self.x + 1

    def __setattr__(self, name, value):
        if 'history' in self.__dict__:
            self.history[name].append(value)
        self.__dict__[name] = value # self.__dict__['history'] = value
        print('Namespace now:', self.__dict__)

    def all_attributes(self):
        print('History of attributes:')
        for name, value in sorted(self.history.items()):
            print(f'{name} had values: {value}')



o = H()
o.x = 5
o.increment()
o.all_attributes()

o.y = 10
o.y += 10
o.all_attributes()


class D:
    def __init__(self):
        self.deleted = {}

    def __delattr__(self, name):
        self.deleted[name] = self.__dict__[name]
        del self.__dict__[name]

    def history(self):
        print('Deleted attributes and the last values they were binded to: ', self.deleted)


x = D()
x.apple = 1
x.orange = 2
x.apple = 10
print(x.__dict__)

del x.apple
print(x.__dict__)
x.history()
del x.orange

x.history()


######################## static method ###########################

def f():
    pass


class C:
    def __init__(self, a):
        self.a = a

    def __call__(self):
        self.a*=self.a
        print('I am being called')


obj = C(10)

print(obj.a)
print(obj)

# calling
obj()
print(obj.a)


######################## static method ###########################

def convert_to_float(integer):
    return float(integer)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # @staticmethod
    # def convert_to_float(integer):
    #     return float(integer)

    def __add__(self, other):

        return Point(convert_to_float(self.x+other.x), convert_to_float(self.y+other.y))


p = Point(5, 10)
print(p)

p2 = Point(5, 10)
print(p+p2)



