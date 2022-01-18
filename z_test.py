# pylint: disable=all
from money import Money

a = Money(10, 10, 10, 10, 10)

# t = FundsControl(a)
# print('t', t.get_balance())

# cus = Money(0, 0, 0, 0, 1)
# print('insert', cus.balance)

# p = 300
# print('price', p)

# ch = t.transaction(cus, p)

# if ch:
#     print('bal-', t.get_balance(), 'ch-', ch.balance)
# else:
#     print('bal-', t.get_balance())


# Amount of money to begin with
# number of coins
money_0 = Money(20, 20, 20, 10, 10)

# Grid of the machine
rows_0 = 3
columns_0 = 3

# some beggining items
# all prices are in stotinki
list_items_0 = [
    {
        'name': 'Name1',
        'number': 5,
        'price': 100
    },
    {
        'name': 'Name2',
        'number': 5,
        'price': 120
    },
    {
        'name': 'Name3',
        'number': 5,
        'price': 130
    },
    {
        'name': 'Name4',
        'number': 5,
        'price': 50
    },
    {
        'name': 'Name5',
        'number': 5,
        'price': 80
    },
    {
        'name': 'Name6',
        'number': 5,
        'price': 180
    },
    {
        'name': 'Name7',
        'number': 5,
        'price': 200
    },
    {
        'name': 'Name8',
        'number': 5,
        'price': 250
    },
    {
        'name': 'Name9',
        'number': 5,
        'price': 340
    },
    {
        'name': 'Name10',
        'number': 5,
        'price': 400
    }
]


#
# some tests
#

list_art = [
    'Art1',
    'Art2',
    'Art3',
    'Art4',
    'Art5',
    'Art6',
    'Art7',
    'Art8',
    'Art9',
    'Art10',
    'Art11',
    'Art12',
    'Art13',
    'Art14',
    'Art15',
    'Art16',
    'Art17',
    'Art18',
    'Art19',
    'Art20',
    'Art21'
]

# test1 = Machine(columns_0, rows_0)

# for i in range(columns_0):
#     for j in range(rows_0):
#         test1.add_item(list_art[j*columns_0+i], 2, 100, i+1, j+1)

# test1.print_all()

#
#
#


# Load parameters
# must be from json files


# current = Machine(money_0, columns_0, rows_0)
#
# for i in range(columns_0):
#     for j in range(rows_0):
#         item = Item(
#             list_items_0[j*columns_0+i]['name'],
#             list_items_0[j*columns_0+i]['number'],
#             list_items_0[j*columns_0+i]['price'],
#             i+1,
#             j+1
#         )
#         current.add_item(item)
