# pylint: disable=C0114, C0115, C0116, W1514, C0301

import json
from machine import Machine
from item import Item
from money import Money


# Save and load json files

def save_json(machine: Machine):
    inventory_file = 'inventory.json'
    money_file = 'money.json'

    inventory_data = {
        "columns": machine.columns,
        "rows": machine.rows,
        "items": [
            {
                "name": item.name,
                "number": item.number,
                "price": item.price,
                "column": item.column,
                "row": item.row
            } for item in sum(machine.grid_items, [])
        ]
    }
    with open(inventory_file, 'w') as outfile:
        json.dump(inventory_data, outfile, indent=4)

    money_data = {
        "st_10": machine.money.st_10,
        "st_20": machine.money.st_20,
        "st_50": machine.money.st_50,
        "st_100": machine.money.st_100,
        "st_200": machine.money.st_200
    }
    with open(money_file, 'w') as outfile:
        json.dump(money_data, outfile, indent=4)


def load_json():
    inventory_file = 'inventory.json'
    money_file = 'money.json'

    with open(inventory_file) as json_file:
        inventory_data = json.load(json_file)

    with open(money_file) as json_file:
        money_data = json.load(json_file)

    new_current = Machine(
        Money(
            money_data['st_10'],
            money_data['st_20'],
            money_data['st_50'],
            money_data['st_100'],
            money_data['st_200']
        ),
        inventory_data['columns'],
        inventory_data['rows']
    )

    for item_d in inventory_data['items']:
        new_item = Item(
            item_d['name'],
            item_d['number'],
            item_d['price'],
            item_d['column'],
            item_d['row']
        )
        new_current.add_item(new_item)

    # for column in range(inventory_data['columns']):
    #     for row in range(inventory_data['rows']):
    #         item = Item(
    #             inventory_data['items'][row*columns_0+column]['name'],
    #             inventory_data['items'][row*columns_0+column]['number'],
    #             inventory_data['items'][row*columns_0+column]['price'],
    #             column+1,
    #             row+1
    #         )
    #         new_current.add_item(item)

    return new_current


# Operations

def buying(machine: Machine):
    location = input('Enter row number and column letter: ').lower()
    column = 0
    row = 0
    if location[0].isalpha():
        column = ord(location[0])-96
        row = int(location[1])
    else:
        column = ord(location[1]) - 96
        row = int(location[0])

    ins_money = list(map(int, input(
        'Enter number of coins (space separated numbers for coins of 0.10, 0.20, 0.50, 1, 2 lv): ').split()))

    amount = Money(
        ins_money[0],
        ins_money[1],
        ins_money[2],
        ins_money[3],
        ins_money[4]
    )

    out = machine.buy_item([column, row], amount)
    if out:
        print('Purchase compleated!')
        if out.balance > 0:
            print(f'Your change is {out.balance/100} lv.')
    else:
        print('Purchase cannot be completed!')

    save_json(machine)


# Main

current = load_json()

while True:
    print('\nMachine balance -', round(current.money.balance/100, 2))
    current.print_items()
    buying(current)
    again = input('Again (y/n): ')
    if again.lower() == 'n':
        break


save_json(current)
