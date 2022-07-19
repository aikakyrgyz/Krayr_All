import math


class Vector:
    def __init__(self, *args):
        'Sets the self.coords to the tuple containing all of the arguments passed'
        self.coords = args

    def __len__(self):
        'Returns the length of the coordinate tuple'
        # Note: __len__ method is required to return an integer type value
        return len(self.coords)

    def __bool__(self):
        'Returns true if at least one value in the tuple is not 0, else False'
        # Note: __bool__ method is not required to return only a bool type, it can return any type
        return not all(v == 0 for v in self.coords)
        # same as:
        # return any( v!=0 for v in self.coords )

    def __repr__(self):
        '''The convention for __repr__ is that it returns a string,
        which if passed as the argument to the eval function, would produce an object with the same state'''
        # Note: you can make it to just return a string in any format you want
        # Called when repr(object) is called
        return 'Vector(' + ','.join(str(c) for c in self.coords) + ')'

    def __str__(self):
        '''Called when str(object) is called'''
        return '(' + str(len(self)) + ')' + str(list(self.coords))  # using +

    def distance(self):
        'Returns the distance of the vector from the origin/(0,0)'
        return math.sqrt(sum(v ** 2 for v in self.coords))

    def __lt__(self, right):
        'Returns a bool when two objects are compared: < '
        if type(right) is Vector:
            return self.distance() < right.distance()
        elif type(right) in (int, float):
            return self.distance() < right
        else:
            return NotImplemented


    def __gt__(self, right):
        'Returns a bool when two objects are compared: > '
        if type(right) is Vector:
            return self.distance() > right.distance()
        elif type(right) in (int, float):
            return self.distance() > right
        else:
            return NotImplemented

    def __eq__(self, right):
        'Returns a bool when two objects are compared: == '
        return self.coords == right.coords

    def __le__(self, right):
        'Returns a bool when two objects are compared: <= '
        return self < right or self == right

    def __ge__(self, right):
        'Returns a bool when two objects are compared: >= '
        return self > right or self == right

    def __neg__(self):
        'Returns a new vector object when an object is negated: -'
        return Vector(*(-c for c in self.coords))

    def __pos__(self):
        'Returns the vector itself on which the + is being applied to'
        return self

    def __abs__(self):
        'Returns a new vector when abs(object) function is called'
        return Vector(*(abs(c) for c in self.coords))

    def __add__(self, right):
        'Returns a new object when two objects are added'
        if type(right) not in (Vector, int, float):
            return NotImplemented
        if type(right) in (int, float):
            return Vector(*(c + right for c in self.coords))
        else:
            assert len(self) == len(right), 'Vector.__add__: operand self(' + str(
                self) + ') has different dimension that operand right(' + str(right) + ')'
            return Vector(*(c1 + c2 for c1, c2 in zip(self.coords, right.coords)))

    def __radd__(self, left):
        'Returns a new object when two objects are added, called when __add__ fails to evaluate an expression'
        if type(left) not in (int, float):  # see note below
            return NotImplemented
        return Vector(*(left + c for c in self.coords))
        # same as
        # return left + right

    def __iadd__(self,right): # obj1 += obj2, ex: obj1 += [1, 2, 3]
        'Returns a new object when two objects are added with +=  '
        if type(right) not in (Vector,int,float):
            return NotImplemented
        if type(right) in (int,float):
            return Vector( *(c+right for c in self.coords))
        else:
            assert len(self) == len(right), 'Vector.__add__: operand self('+str(self)+') has different dimension that operand right('+str(right)+')'
            return Vector( *(c1+c2 for c1,c2 in zip(self.coords,right.coords)))




########## __init__ ##########
v = Vector(0,0)
print(v.coords) # (0, 0)

v.coords = (1,1)
print(v.coords) # (1, 1)

v.__init__(5,5,5,5,5)   # We can call __init__ explicitly, like any other method
print(v.coords) # (5, 5, 5, 5, 5)

########## __len__ ##########
v = Vector(0,0)
print(len(v)) # 2

########## __str__ ##########
v = Vector(0,0) #( 2)[0, 0]
print(v)

########## __repr__ ##########
v = Vector(0,0)
new_v_str = repr(v)
new_v = eval(new_v_str) # copy of v is created
print(type(new_v)) # <class '__main__.Vector'>
print(new_v.coords) # (0, 0)


########## __lt__ ##########
x = Vector(0,0)
y = Vector(2,2)
print(x < y) # True
print(x < 10) # True
print(10 < x) # False


########## __gt__ ##########
x = Vector(0,0)
y = Vector(2,2)
print(x > y) # False
print(10 > x) # True
print(1 > y) # False
print(x > [1, 2])

########## __eq__ ##########
x = Vector(0,0)
y = Vector(2,2)
print(x == y) # False
z = Vector(2, 2)
print(y == z) # True


########## __le__ ##########
x = Vector(0,0)
y = Vector(2,2)
print(x <= y) # True
z = Vector(2, 2)
print(y <= z) # True


########## __ge__ ##########
x = Vector(0,0)
y = Vector(2,2)
print(x >= y) # False
z = Vector(2, 2)
print(y >= z) # True


########## __neq__ ##########
v = Vector(1,2,3)
print(v) # (3)[1, 2, 3]
print(-v) # (3)[-1, -2, -3]
print(v) # (3)[1, 2, 3]

########## __pos__ ##########
v = Vector(1, -2, 3)
print(v) # (3)[1, -2, 3]
print(+v) # (3)[1, -2, 3]


########## __abs__ ##########
v = Vector(-1, -2, 3)
print(abs(v)) # (3)[1, 2, 3]


########## __add__ ##########
v1 = Vector(0,1)
v2 = Vector(2,2)
print(v1+v2) # (2)[2, 3]


####### __radd__ #######
v = Vector(0,0)
print(1+v) # (2)[1, 1]
# 1.__add__(v) --> type(1).__add__(1, v) --> int.__add__(1, v) -> int class does not know how to add int to Vector, so __radd__ is called (radd == right add)
# -> v + 1 -> v.__radd__(1) --> type(v).__radd__(v, 1) --> Vector.__radd__(v, 1)



####### __iadd__ #######
v = Vector(0,0)
v += Vector(2, 3)
print(v) # (2)[2, 3]







