# pylint: disable=C0114, C0115, C0116

from machine import Machine
from item import Item
from money import Money
from funds import FundsControl

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
        'name': 'Art1',
        'number': 5,
        'price': 100
    },
    {
        'name': 'Art2',
        'number': 5,
        'price': 120
    },
    {
        'name': 'Art3',
        'number': 5,
        'price': 130
    },
    {
        'name': 'Art4',
        'number': 5,
        'price': 50
    },
    {
        'name': 'Art5',
        'number': 5,
        'price': 80
    },
    {
        'name': 'Art6',
        'number': 5,
        'price': 180
    },
    {
        'name': 'Art7',
        'number': 5,
        'price': 200
    },
    {
        'name': 'Art8',
        'number': 5,
        'price': 250
    },
    {
        'name': 'Art9',
        'number': 5,
        'price': 340
    },
    {
        'name': 'Art10',
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


current = Machine(columns_0, rows_0)
funds = FundsControl(money_0)


for i in range(columns_0):
    for j in range(rows_0):
        current.add_item(
            list_items_0[j*columns_0+i]['name'], 
            list_items_0[j*columns_0+i]['number'], 
            list_items_0[j*columns_0+i]['price'], 
            i+1, 
            j+1
            )


current.print_all()


