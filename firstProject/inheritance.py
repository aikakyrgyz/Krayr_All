# Attention: these notes continue the lecture from Monday class
# see the CONTINUED section:

# Inheritance provides a convenient mechanism for building groups of related abstractions.
# It allows us to create a type of hierarchy in which each type inherits attributes from
# the types above it in the hierarchy.
# This opens the door to what are usually called frameworks - hierarchies of classes that
# specialize behavior by overriding attributes lower in the hierarchy.

# Some important bullets:
# 1. Superclasses are listed in parentheses in a class header
# 2. Classes inherit attributes from their superclasses
# 3. Instances inherit attributes from all accessible classes
# 4. Logic changes are made in subclasses, not the superclasses (overriding)


class Animal: # superclass or parent class or base class
    eyes = 2

    def __init__(self, name, color, continent):
        self.name = name
        self.color = color
        self.continent = continent

    def __str__(self):
        return 'Animal Name:' + self.name

    def walk(self):
        return f'{self.name} is walking'

    def breath(self):
        return f'{self.name} is breathing'

    def eat(self, food):
        return f'{self.name} is eating {food}'


# Mammal inherits all of the methods and attributes from Animal class
class Mammal(Animal): # subclass or child or derived class
    baby_food = 'milk'

    def __init__(self, name, color, continent, under_water):
        # calling a method from a parent class
        super().__init__(name, color, continent)
        self.under_water = under_water

    def feed(self):
        return f'{self.name} is feeding the baby with {Mammal.baby_food}'


class Bird(Animal):
    num_wings = 2

    # def __init__(self, name, color, continent):
    #     super().__init__(name, color, continent)

    def fly(self):
        if self.name in ('chicken', 'hen', 'penguin'):
            return f'Oops this kind of bird cannot fly'
        return f'{self.name} is flying in the sky'

# Another example

animal = Animal('zebra', 'black and white', 'Africa')
print(animal)

mammal = Mammal('whale', 'grey', 'Pacific Ocean', 'True')
print(mammal)
print(mammal.name)
print(mammal.under_water)
print(mammal.feed())
print(mammal.eat('plankton'))
print(mammal.eyes)

bird = Bird('seagul', 'white', 'All')
print(bird)
print(bird.name)
print(bird.continent)
print(bird.fly())
bird2 = Bird('penguin', 'white', 'Antarctica')
print(bird2.fly())
print(bird2.eat('worm'))
print(bird.eyes)


# print(bird.baby_food)

# Attribute Error since the baby_food is
# defined in the Mammal class, but the Bird only inherits from
# the Animal class, not the mammal class

# Note: The parent class does not know anything about its child classes
# so if you did something like animal.baby_food it would raise an error, since the parent class
# DOES NOT inherit from its child classes nor it has the access to them.


# So, Each class "KNOWS" its base class(es), but a class DOES not "KNOW" its derived class(es): the arrow
# is one way.
# Fundamentally, what inheritance is about is writing small derived classes that
# reuse attributes from base classes in a natural way. The attribute location
# process is captured by augmenting the meaning of The Fundamental Equation of
# Object-Oriented Programming for class inheritance hierarchies.


###################### stopped here #######################























###################### !!!!!!!!! ##########################
###################### CONTINUED ##########################

# when we define a class with the below syntax, it is the same as writing
# class MyClass(object) -> therefore, all of the classes inherit from the object class.
class MyClass:
    pass

print('ATTRIBUTE LOOKUP')


class N:
    def __str__(self):
        print('str method in N')

class P(N):
    x = 10


class C(P):
    pass

obj = C()

print(C.__dict__)
print(P.__dict__)
print(N.__dict__)
print(obj.__dict__)

print(obj.x)

print(obj.__str__())


# How are the attributes and methods are looked up in single inheritance
"""
 1) Python first tries to find the attribute in the instance object.

 2) If Python fails, it next tries to find the attribute in the class object
      from which the instance was constructed (the type function provides this
      information: we can compute the class from which any objects is
      constructed).

 3) If Python fails, it tries to find the attribute in the base class of the
      class from which the instance was constructed;

 4) If Python fails, it next tries to find it in the base class of that class,
      ... and continues until it reaches the object class at the root of the
      inheritance hierarchy.

 5) If Python fails to find the attribute in the object class, it calls
      __getattr__ in the original class of the object (and if it is not there,
      it repeats searching for that method in the hierarchy). The object class
      at the root of the hierarchy defines __getattr__ to raise an AttributeError exception.
"""

# Some inheritance design rules:
# 1) If a class adds an attribute to an object (e.g., in __init__) then methods
# defined in only that class should access the attribute DIRECTLY by name.

# 2) If other classes (including derived/subclasses) need to access/update the
# information stored in that attribute, then the class defining the attribute
# should also define METHODS that do these jobs, which the other class should
# call.


################### QUESTIONS ##################

# 1

class B:
    y = 100
    def __init__(self):
        self.a = 1

class D(B):
    def __init__(self):
        self.a = 2

b = B()
d = D()
print(b.a) # 1
print(d.a) # 2
print(d.__dict__)
print(D.__dict__)
print(B.__dict__)
print(d.y)



# 2


class Parent:
    def m1(self):
        print('m1 in Parent')

    def m2(self):
        # self == o
        print('m2 in Parent')
        # print(type(self))
        self.m1()   # Child.m1() # o.m1()


class Child(Parent):
    def m1(self):
        print('m1 in Child')

    def m2(self):
        print('m2 in Child')
        Parent.m2(self)  # or the call super().m2()


o = Child()
o.m2()

print('---------------')
# how to make it print:

# m2 in Child
# m2 in Parent
# m1 in Parent


class Parent:
    def m1(self):
        print('m1 in Parent')

    def m2(self):
        # self == o
        print('m2 in Parent')
        # print(type(self))
        Parent.m1(self)   # Child.m1() # o.m1()


class Child(Parent):
    def m1(self):
        print('m1 in Child')

    def m2(self):
        print('m2 in Child')
        Parent.m2(self)  # or the call super().m2()


o = Child()
o.m2()


class Counter:
    # Class variable
    hierarchy_depth = 1
    counter_num = 0

    def __init__(self, init_value=0):
        assert init_value >=0, 'Init value must be >= 0'
        # instance variable
        self._value = init_value
        Counter.counter_num +=1

    def __str__(self):
        return str(self._value)

    def reset(self):
        self._value = 0

    def increment(self):
        self._value +=1

    def cur_value(self):
        print(self._value)

# c5 = Counter(-3) # raises an Assertion Error (an exception )

c1 = Counter()
c1.cur_value()
c1.increment()
c1.increment()
c1.cur_value()
c1.increment()
c1.cur_value()
c1.reset()
c1.cur_value()
print(c1.__dict__)
print(Counter.__dict__)
c2 = Counter()
c2.increment()
c3 = Counter()
c3.increment()
c3.increment()

print(Counter.counter_num)

# Counter 1, 2, 3, 4, 5
# Modular Counter, modulus = 10 -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, ...
# ModuleCounter is a Counter
# Single Inheritance


class ModularCounter(Counter):
    hierarchy_depth = Counter.hierarchy_depth + 1
    modular_counter_num = 0

    def __init__(self, init_value, modulus):
        assert modulus >=1, 'Modulus must be greater than 1'
        assert 0 <= init_value < modulus, 'Initial value must be between [0, modulus)'
        # print(ModularCounter.__bases__)
        Counter.__init__(self, init_value)
        # super().__init__(init_value)
        # Note: do NOT pass self when calling a method through super
        self._modulus = modulus
        ModularCounter.modular_counter_num +=1
        # NOT self.modular_counter_num +=1

    def __str__(self):
        return f'{self._value}->{self._modulus}'

    def modulus(self):
        return self._modulus

    def increment(self):
        if self._value == self._modulus:
            self.reset()
        else:
            super().increment()
            # Counter.increment(self)



m = ModularCounter(0, 10)
m.increment()
m.increment()
m.increment()
m.increment()
m.increment()
m.increment()
m.increment()
m.increment()
m.increment()
m.increment()
m.cur_value()
m.increment()
m.cur_value()
m.increment()
m.cur_value()
m2 = ModularCounter(0, 5)
m2.increment()
m2.increment()
m2.increment() # 3
m2.increment() # 4
m2.increment() # 5
m2.increment()
m2.cur_value()

m3 = ModularCounter(0, 5)
m4 = ModularCounter(0, 1)


# m5 = ModularCounter(0, 0) # AssertionError: Modulus must be greater than 1


# m6 = ModularCounter(100, 10) # AssertionError: Initial value must be between [0, modulus)


print(ModularCounter.modular_counter_num) # 4


# Useful Resource: https://github.com/milaan9/06_Python_Object_Class/blob/main/003_Python_Inheritance.ipynb



