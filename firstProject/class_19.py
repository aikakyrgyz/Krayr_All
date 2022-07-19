
# if you also want a pretty output on your console :)
# go to you terminal, do not open python shell
# input the command pip install rich, and this should work, if it does not, send me a message on discord
from rich import print
from rich import pretty
pretty.install()

# static methods

# A method is defined static if it does not have a self parameter. You can look at this as a helper function.

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    @staticmethod
    def from_polar(dist, angle):
        return Point(dist * math.cos(angle), dist * math.sin(angle))

    @staticmethod
    def _distance(x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    def dist(self, other):
        return Point._distance(self.x, self.y, other.x, other.y)

        # return self._distance(self.x, self.y, other.x, other.y)
        # -> type(self)._distance(...)-> Point._distance(...)

        # return other._distance(...)




a = Point(0, 1)
b = Point.from_polar(1.0, math.pi/4) # create point in its Polar representation
print(b.x, b.y)


c = Point(0, 5)

print('The distance between a and c is:', a.dist(c))



# # keyword, positional arguments
# def f(*args):
#     print(args)
#
# f(1, 2, 3, 4, 5)
# f(1)
#
#
# def f(a, default = 2):
#     print(a)
#     print(default)
# f(5, 10)
#
#
# # positional arguments: they are separated by coma
#
# # keyword arguments: passed with an equal sign
# # print('Aika', end = '.')
#
# def f(**kargs):
#     print(kargs)
#
#
# f(a = 2, b = 3, default = 'okay', end = '=')



# Method overloading
# Useful resource you can refer to: https://github.com/milaan9/06_Python_Object_Class/blob/main/004_Python_Operator_Overloading.ipynb


class Vector:
    def __init__(self, *args):
        self.coords = args


    def __len__(self):
        # Note: must return an integer
        print('Calling __len__ method')
        return len(self.coords)

    def __bool__(self):
        'returns True if at least one coordinate is not equal to 0'
        # Note: the bool method does not have to return only a bool type
        print('Calling __bool__ method')
        return any(v!=0 for v in self.coords)
        # return not all(v == 0 for v in self.coords)

    def __str__(self):
        # Note: str must return a string
        return  f'({len(self.coords)}){list(self.coords)}'

    def __repr__(self):
        # Note: repr must return a string
        # repr returns the representation of that same object as a string,
        # so that later we can create an new object from this string
        return f"Vector({','.join([str(v) for v in self.coords])})"


    def distance(self):
        'calculates the distance from the origin'
        print('The distance of ', self, ' is ', math.sqrt(sum(v**2 for v in self.coords)))
        return math.sqrt(sum(v**2 for v in self.coords))

    def __lt__(left, right):
        return left.distance() < right.distance()

        # left.distance -> returns -> left_distance
        # right.distance -> returns -> right_distance
        # left_distance < right_distance
        # left_distance.__lt__(right_distance)
        # type(left_distance).__lt__(left_distance, right_distance)
        # float.__lt__(left_distance, right_distance)

    def __gt__(left, right):
        # return left.distance() > right.distance()
        # want to determine left > right
        return right < left
        # right.__lt__(left)


    def __ge__(left, right):
        # >=
        return left.distance() >= right.distance()

    def __le__(left, right):
        # left <= right
        return right >= left # uses the __ge__
        # return left.distance() <= right.distance() # uses just regular comparison by looking at the distance from the origin


    def __eq__(left, right):
        # Note: if __eq__ is not defined, then it tries to subsitute it with is
        # v1 == v2 -> v1.__eq__(v2) -> v1 is v2
        return left.distance() == right.distance()

    def __neq__(left, right):
        return left.distance()!= right.distance
        # return not left == right



v = Vector(0, 0)
print(v.coords)

v.coords = (1, 2)
print(v.coords)

v2 = Vector(0, 0, 0, 0, 0)
print(v2.coords)


v2.__init__(0, 0, 0) # call init explicitly, like any other method, redefining coords variable
print(v2.coords)


print(len(v)) # 2
print(len(v2)) # 3


def len(x):
    if type(x) is int:
        raise TypeError(f'{x} object does not have a len method within it')
    return x.__len__()



def test(x):
    print(f'{x} boolean equivalent is: ')
    if x: # tries to call the bool method within the class of the object x
            # if the __bool__ method is not there it calls the __len__ method
        print(True)
    else:
        print(False)

# print(v) # <__main__.Vector object at 0x7f7f2e792df0>
print('Executing  test function')
v = Vector(0, 0)
test(v)

v = Vector(0, 0, 0)
print(len(v)) # 3
test(v) # True, cause 3 > 0

v = Vector()
test(v) # False

print(bool(v))
test(v)

v = Vector(0, 2, 1)
# calling the __str__ method

print(v) # <__main__.Vector object at 0x7fd0e4f9d340>
# after redifining __str__ method:
print(v) # (3)[0, 2, 1]

# calling __repr__ method
# print(repr(v))
#
# y = repr(v)
#
# v3 = eval(y)
# print(v3.coords)
# v3 = Vector(0, 2, 1)
# eval('Vector(0,2,1)')


# let's say the __str__ methods is not defined and I try to print my v (i.e. calling str method)

# print(v3) # Vector(0,2,1), it will call the __repr__ method, as a replacement for __str__ method

    # when calling for a list
    # [1, 2, 3, 4, 5].__len__()
    # type([1, 2, 3, 4, 5]).__len__([1, 2, 3, 4, 5])
    # list.__len__([1, 2, 3, 4, 5])

    # when calling for 1
    # 1.__len__()
    # type(1).__len__(1)
    # int.__len__(1)
    # since int class does not define len method, TypeError is raised



# Remember: len function can only be used for iterables


# print('Using the len function that we defined', len([1, 2, 3, 4, 5]))
#
# print('Using the len function we defined for an int', len(1))


############### Relational operators ##############


####################### before we defined __lt__ method ######################
v = Vector(0, 0)
v2 = Vector(1, 2)

print(1 < 2)

# 1.__lt__(2)
# type(1).__lt__(1, 2)
# int.__lt__(1, 2)
# evaluates ...


# print(v < v2) # '<' not supported between instances of 'Vector' and 'Vector'
# v.__lt__(v2)
# type(v).__lt__(v, v2)
# Vector.__lt__(v, v2)
# but the __lt__ is not defined, so it raises a TypeError



# print(v < 10) #  '<' not supported between instances of 'Vector' and 'int'

# print(10 < v) # '<' not supported between instances of 'int' and 'Vector'

########################### after we defined __lt__ method #######################################

v = Vector(0, 0)
v2 = Vector(5, 5)

print('Is v closer to the origin:', v < v2) # trying to call __lt__

####################### before we defined __gt__ method ######################

print('Is v farther from the origin: ', v > v2) # trying to call __gt__

# even if the __gt__ method is not defined, it is going to call the __lt__ method


# v > v2 -----> v2 < v --> v2.__lt__(v)

####################### after we defined __gt__ method ######################

print('Is v farther from the origin: ', v > v2) # trying to call __gt__, it is found now, since we defined it


#######################  before we defined __ge__ method ######################

print(v >= v2) # '>=' not supported between instances of 'Vector' and 'Vector'
# raises an error since we need to define __ge__ method, it cannot use the __lt__ or __gt__ methods


####################### after we defined __ge__ method ######################

print('The distance of v from the origin is >= v2: ', v >= v2) # False

#######################  before we defined __le__ method ######################

print(v <= v2) # but we still try to call the __le__ method

# v.__le__(v2)
# Vector.__le__(v, v2)

# 1. It tries to look for the __le__ method
# 2. It does not find it
# 3. Python raises an internal error that it tries to handle itself first
# 4. It tries to look for __ge__ method
# 5. Since our __ge__ method is defined, it uses it, by v2.__ge__(v) -> v2 >= v


#######################  define __eq__ method ######################
v1 = Vector(1, 1)
v2 = Vector(2, 2)
print('Is v1 has the same distance from the origin as does v2: ', v1 == v2)  # False

v1 = Vector(1, 1)
v2 = Vector(1, 1)

print('Is v1 has the same distance from the origin as does v2: ', v1 == v2)  # True


####################### before defining __neq__ method ######################
v1 = Vector(1, 1)
v2 = Vector(1, 1)

print('Is v1 does not have the same distance from the origin as does v2: ', v1 != v2)  # False # even though __neq__
# is not defined, it calls the __eq__ method and negates it


####################### after defining __neq__ method ######################

v1 = Vector(1, 1)
v2 = Vector(1, 1)

print('Is v1 does not have the same distance from the origin as does v2: ', v1 != v2)  # False # calls the __neq__ method







