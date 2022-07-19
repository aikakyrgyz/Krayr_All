

from collections import defaultdict
# Part 1
def students_gpas(students: list, gpas: list) ->dict:
    d = dict()
    for student, gpa in zip(students, gpas):
        d[student] = gpa
    return d
    # using comprehension
    # d = {student:gpa for student, gpa in zip(students, gpa)}
    # print(d)

def runners_places(runners: list) -> dict:
    return {runner:place for place, runner in enumerate(runners, 1)}

def min_value(l: list, f) -> int:
    # return min([f(v) for v in l])
    return sorted([f(v) for v in l])[0]

    # print(f) # [2, 1, 0, 1, 2]
    # l = min(l)
    # return l


'''
{ 
'Carl': [('Intel', 30, 40), ('Dell', 20, 50), ('Intel', -10, 60), ('Apple', 20, 55)],
'Barb': [('Intel', 20, 40), ('Intel', -10, 45), ('IBM', 40, 30), ('Intel', -10, 35)],
'Alan': [('Intel', 20, 10), ('Dell', 10, 50), ('Apple', 80, 80), ('Dell', -10, 55)],
'Dawn': [('Apple', 40, 80), ('Apple', 40, 85), ('Apple', -40, 90)]
}
'''
# Part 2
def stocks(db: {str: [(str, int, int)]}) -> {str}:
    # 1
    return {stock_name for transaction in db.values() for stock_name, share, price in transaction}

    # 2
    # s = set()
    # for name, transaction in db.items():
    #     for stock_name, share, price in transaction:
    #         s.add(stock_name)

    # 3
    # return {tuple[0] for value in db.values() for tuple in value}
    # return {price for transaction in db.values() for stock_name, share, price in transaction}


def clients_by_volume(db: {str: [(str, int, int)]}) -> [str]:
    # return sorted(db.keys(), key = lambda client: (sum([abs(share) for stock_name, share, price in db[client]])))

    # return a dictionary where each key is the name of the client
    # and the value is the total number of shares for that client
    # {'Carl': 80, 'Barb': 80, 'Alan': 120}
    d = dict()

    for client, transaction in db.items():
        total = 0
        for stock_name, share, price in transaction:
            total += abs(share)
        d[client] = total
    # print(sorted(d.items(), key = (lambda t: t[1]), reverse = True))
    print(sorted(d.items(), key = (lambda t: (-t[1], t[0]))))


def stocks_by_volume(db: {str: [(str, int, int)]}) -> [(str, int)]:
    #  [('Apple',220), ('Intel',100), ('Dell',40), ('IBM',40)]
    print(stocks(db))
    return sorted([(stock_name, sum([abs(shares) for transactions in db.values() for stock, shares, price in transactions if stock == stock_name])) \
                   for stock_name in stocks(db)], key = lambda t: (-t[1], t[0]))




def by_stock(db: {str: [(str, int, int)]}) -> {str: {str: [(int, int)]}}:
    '''
    {
    'Intel': {'Carl': [(30, 40), (-10, 60)], 'Barb': [(20, 40), (-10, 45), (-10, 35)],  'Alan': [(20, 10)]},
    'Dell': {'Carl': [(20, 50)], 'Alan': [(10, 50), (-10, 55)]},
    'Apple': {'Carl': [(20, 55)], 'Alan': [(80, 80)], 'Dawn': [(40, 80), (40, 85), (-40, 90)]},
    'IBM': {'Barb': [(40, 30)]}
    }
    '''

    outer_d = defaultdict(dict)
    #  {:{}}
    # stocks(db) -> {'Intel', 'Dell', 'Apple', 'IBM'}
    for stock_name in stocks(db):
        inner_d = defaultdict(list)
        for client, transactions in db.items():
            for stock, shares, price in transactions:
                if stock == stock_name:
                    inner_d[client].append((shares, price))
                    outer_d[stock_name] = dict(inner_d)
    return dict(outer_d)


    ########################################
    #
    # result_dict = defaultdict(lambda: defaultdict(list))
    # for client, transactions in db.items():
    #     for stock, shares, price in transactions:
    #         result_dict[stock][client].append((shares, price))
    # return {key:{key2:value2 for key2, value2 in value.items()} for key, value in result_dict.items()}




def summary(db: {str: [(str, int, int)]}, prices: {str: int}) -> {str: ({str: int}, int)}:

    """
    {
    'Carl': ({'Intel': 20, 'Dell': 20, 'Apple': 20}, 3700),
    'Barb': ({'IBM': 40}, 2600),
    'Alan': ({'Intel': 20, 'Apple': 80}, 6800),
    'Dawn': ({'Apple': 40}, 2800)

    {'IBM':65, 'Intel':60, 'Dell':55, 'Apple':70}
    """

    def worth(hold) -> int:
        return sum(shares * prices[stock_name] for stock_name, shares in hold.items())


    holdings = defaultdict(lambda: defaultdict(int))
    for client, transactions in db.items():
        for stock_name, shares, _ in transactions:
            holdings[client][stock_name] += shares
    print()
    print(dict(holdings))
    print()

    return {client: ({stock: amount for stock, amount in holdings[client].items() if amount!=0}, worth(holdings[client])) for client in holdings}






if __name__ == '__main__':
    print('Testing students_gpa:')
    students = ['bob', 'carol', 'ted', 'alice']
    gpas = [3.0, 3.2, 2, 8, 3.6]
    print(students_gpas(students, gpas))

    print('Testing runners_places')
    runners = ['bob','carol','ted','alice']
    print(runners_places(runners))

    def func(x):
        return abs(x)

    print(min_value([-2, -1, 0, 1, 2], func))



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

    # comment this part out if you want to test it yourself
    import driver

    # driver.default_file_name = 'tests1.txt'
    # #     driver.default_show_traceback = True
    # #     driver.default_show_exception = True
    # #     driver.default_show_exception_message = True
    # driver.driver()