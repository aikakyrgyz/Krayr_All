


# types of variables


# 1. local variables
# 2. instance variables
# 3. class variables
# 4. global variables


# Class objects:
# 1. Class objects store methods and/or class variables
# 2. The attributes of the class are accessed by class_name.attribute_name (but only if that attribute is defined)
# 3. Class_Name.__dict__ is a dictionory storing Class_Name's attributes, methods


# Instance objects:
# 1. are defined by object_name = ClassName()
# 2. The init initializes the instance object's attributes
# 3. the attributes are accessed by object_name.attribute_name
# 4. object_name.__dict__ is a dictionary storing object_name's attributes


# classes

# each type in Python belongs to some class
# string = 'word'
# print(type(string))
#

# A class is like a blueprint for an object

# car, attributes: wheel, tires, doors, seats
# car, methods   : drive(), stop(), accelerate()



# A class vegetables
# attributes: color, taste, vitamins
# methods: grow()


# Student
# attributes: name, list of classes, studentID
# methods: study(), attend_classes()


# string:
# attributes: address, list of characters
# methods: split(), startswith()



# in a Class attributes and methods are accessed with a .
class NameClass:
    pass



# class Car:
#     number_of_tires = 4
#     number_of_wheels = 1
#
#     def __init__(self):
#         self.model = 'Mazda'
#         self.year = 2015
#         self.color = 'blue'
#         self.current_speed = 10
#
#     def accelerate(self):
#         print('I am accelarating')
#         self.current_speed +=5
#
#
# my_mazda = Car()
#
# print(my_mazda.model)
# print(my_mazda.current_speed)
# my_mazda.accelerate()
# print(my_mazda.current_speed)


# Usually you don't want to access the attributes of a class directly


class Counter:
    global_counter = 0
    def __init__(self):
        self._count = 0

    def count(self):
        self._count +=1
        x = 10
        print(x)
        return self._count

    def peek(self): # getter method
        return self._count

    def reset(self):
        self._count = 0

c1 = Counter()
c1.count()
print(c1.peek())
c1.count()
c1.count()
print(c1.peek())
c1.reset()
print(c1.peek())
print(c1._count)
print(Counter.__dict__)
print('-----')
print(c1.__dict__)
c2 = Counter()
c2.count()
c2.count()
c2.count()
print(c2.__dict__)


class Person:
    # class variable
    grade = '8th grade'
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def full_name(self):
        return f'{self._first_name} {self._last_name}'



# create an object
p1 = Person('John', 'Blake')
print(p1.get_last_name())
print(p1.get_first_name())
print(p1.full_name())

# p2 is also an object
p2 = Person('Alice', 'S')

# p3
p3 = Person('Justin', 'W')

print(p3.get_first_name())


print(p1.grade)
print(p2.grade)
print(p3.grade)

print(Person.__dict__)


print(p1.__dict__)
print(p2.__dict__)




































'''
from collections import defaultdict


def stocks(db: {str: [(str, int, int)]}) -> {str}:
    return {stock for transactions in db.values() for stock, _, _ in transactions}


def clients_by_volume(db: {str: [(str, int, int)]}) -> [str]:
    return sorted(db, key=(lambda client: (-sum(abs(shares) for _, shares, _ in db[client]), client)))


def stocks_by_volume(db: {str: [(str, int, int)]}) -> [(str, int)]:
    return sorted(
        [(astock, sum([abs(shares) for transactions in db.values() for s, shares, _ in transactions if s == astock]))
         for astock in stocks(db)],
        key=lambda x: (-x[1], x[0]))


def by_stock(db: {str: [(str, int, int)]}) -> {str: {str: [(int, int)]}}:
    answer = defaultdict(lambda: defaultdict(list))
    for client, transactions in db.items():
        for stock, shares, cost in transactions:
            answer[stock][client].append((shares, cost))
    return {k: {k2: v2 for k2, v2 in v.items()} for k, v in answer.items()}


def summary(db: {str: [(str, int, int)]}, prices: {str: int}) -> {str: ({str: int}, int)}:
    def worth(hold: {str: int}):
        return sum(shares * prices[stock] for stock, shares in hold.items())

    holdings = defaultdict(lambda: defaultdict(int))
    for client, transactions in db.items():
        for stock, buysell, _ in transactions:
            holdings[client][stock] += buysell
    return {client: ({stock: amount for stock, amount in holdings[client].items() if amount != 0},
                     worth(holdings[client])) for client in holdings}
    # or
    return {client: ({stock: amount for stock, amount in holdings[client].items() if amount != 0},
                     sum((shares * prices[stock] for stock, shares in holdings[client].items()))) for client in
            holdings}


if __name__ == '__main__':


    # Note: the keys in this dicts are not specified in alphabetical order
    db1 = {
        'Carl': [('Intel', 30, 40), ('Dell', 20, 50), ('Intel', -10, 60), ('Apple', 20, 55)],
        'Barb': [('Intel', 20, 40), ('Intel', -10, 45), ('IBM', 40, 30), ('Intel', -10, 35)],
        'Alan': [('Intel', 20, 10), ('Dell', 10, 50), ('Apple', 80, 80), ('Dell', -10, 55)],
        'Dawn': [('Apple', 40, 80), ('Apple', 40, 85), ('Apple', -40, 90)]
    }

    db2 = {
        'Hope': [('Intel', 30, 40), ('Dell', 20, 50), ('IBM', 10, 80), ('Apple', 20, 90), ('QlCom', 20, 20)],
        'Carl': [('QlCom', 30, 22), ('QlCom', 20, 23), ('QlCom', -20, 25), ('QlCom', -30, 28)],
        'Barb': [('Intel', 80, 42), ('Intel', -80, 45), ('Intel', 90, 28)],
        'Fran': [('BrCom', 210, 62), ('BrCom', -20, 64), ('BrCom', -10, 66), ('BrCom', 10, 55)],
        'Alan': [('Intel', 20, 10), ('Dell', 10, 50), ('Apple', 80, 80), ('Dell', -10, 55)],
        'Gabe': [('IBM', 40, 82), ('QlCom', 80, 25), ('IBM', -20, 84), ('BrCom', 50, 65), ('QlCom', -40, 28)],
        'Dawn': [('Apple', 40, 92), ('Apple', 40, 98), ('Apple', -40, 92)],
        'Evan': [('Apple', 50, 92), ('Dell', 20, 50), ('Apple', -10, 95), ('Apple', 20, 95), ('Dell', -20, 90)]
    }

    prices1 = {'IBM': 65, 'Intel': 60, 'Dell': 55, 'Apple': 70}

    prices2 = {'IBM': 85, 'Intel': 45, 'Dell': 50, 'Apple': 90, 'QlCom': 20, 'BrCom': 70}

    print('\nTesting stocks')
    print('stocks(db1):', stocks(db1))
    print('stocks(db2):', stocks(db2))

    print('\nTesting clients_by_volume')
    print('clients_by_volume(db1):', clients_by_volume(db1))
    print('clients_by_volume(db2):', clients_by_volume(db2))

    print('\nTesting stocks_by_volume')
    print('stocks_by_volume(db1):', stocks_by_volume(db1))
    print('stocks_by_volume(db2):', stocks_by_volume(db2))

    print('\nTesting by_stock')
    print('by_stock(db1):', by_stock(db1))
    print('by_stock(db2):', by_stock(db2))

    print('\nTesting summary')
    print('summary(db1):', summary(db1, prices1))
    print('summary(db2):', summary(db2, prices2))

    print('\ndriver testing with batch_self_check:')
    import driver

    driver.default_file_name = 'bscq1W22.txt'
    #     driver.default_show_traceback = True
    #     driver.default_show_exception = True
    #     driver.default_show_exception_message = True
    driver.driver()
'''