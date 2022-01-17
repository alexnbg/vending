# pylint: disable=C0114, C0115, C0116

from machine import Machine
from item import Item

trows = 3
tcolumns = 3


dict_art = {
    'Art1': 2,
    'Art2': 2,
    'Art3': 2,
    'Art4': 2,
    'Art5': 2,
    'Art6': 2,
    'Art7': 2,
    'Art8': 2,
    'Art9': 2,
    'Art10': 2,
    'Art11': 2,
    'Art12': 2,
    'Art13': 2,
    'Art14': 2,
    'Art15': 2,
    'Art16': 2,
    'Art17': 2,
    'Art18': 2,
    'Art19': 2,
    'Art20': 2
}

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

test1 = Machine(tcolumns, trows)


for i in range(tcolumns):
    for j in range(trows):
        test1.add_item(list_art[j*tcolumns+i], 2, i+1, j+1)

test1.print_all()
