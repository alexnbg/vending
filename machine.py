# pylint: disable=C0114, C0115, C0116

from item import Item
from money import Money


class Machine:
    def __init__(self,
                 money: Money,
                 columns: int,
                 rows: int
                 ) -> None:
        self.money = money
        self.columns = columns
        self.rows = rows
        self.grid_items = [[0] * columns for i in range(rows)]

    # Buying an item

    def transaction(self, amount: Money, price: int):
        """
        Makes the transaction and returns the change as Money object
        Returns False if the inserted amount is less than the price
        or there are no money to return the change
        """
        diff = amount.balance - price
        change = Money(0, 0, 0, 0, 0)

        if diff == 0:
            self.money = self.money + amount
            return change

        if diff > 0:
            while diff >= 200:
                diff -= 200
                change.st_200 += 1
            while diff >= 100:
                diff -= 100
                change.st_100 += 1
            while diff >= 50:
                diff -= 50
                change.st_50 += 1
            while diff >= 20:
                diff -= 20
                change.st_20 += 1
            while diff >= 10:
                diff -= 10
                change.st_10 += 1

            if change >= self.money:
                return False

            self.money = self.money + amount
            self.money = self.money - change
            return change

        return False

    def buy_item(self,
                 item_location: list,
                 amount: Money):
        """
        Buying the item
        Return False, if there is no item in this location
            or the item is out of stock
            or the inserted amount is not enough
            or there are no money to return change
        Return change as Money object
        and decreases the item number by 1
        """
        item = self.grid_items[item_location[1]-1][item_location[0]-1]
        if not isinstance(item, Item):
            return False
        if item.number < 1:
            return False

        change = self.transaction(amount, item.price)
        if not change:
            return False

        item.number -= 1
        return change

    # Controlling items in the machine grid

    def add_item(self, item: Item):
        """
        Add or replace an item in the grid
        """
        self.grid_items[item.row-1][item.column - 1] = item

    def remove_item(self, item: Item):
        """
        Remove item and place 0 in the empty location
        """
        self.grid_items[item.row-1][item.column - 1] = 0

    # Prints

    def print_items(self):
        """
        Prints a grid with all items (item name, price and amount left)
        """
        print('Items to sell:')
        print(
            ' '*10, ' '.join(
                [f'Column {chr(65+column)}'.center(12)
                 for column in range(self.columns)]
            )
        )
        print()
        for row in range(self.rows):
            print(' '*10, ' '.join(
                [f'{item.name}'.center(12) for item in self.grid_items[row]]
            ))
            print(f'Row {row+1}'.ljust(10), ' '.join(
                [f'price: {round(item.price/100,2)}'.center(12)
                 for item in self.grid_items[row]]
            ))
            print(' '*10, ' '.join(
                [f'left: {item.number}'.center(12)
                 for item in self.grid_items[row]]
            ))

    # for tests

    def print_grid_names(self):
        for row in range(self.rows):
            print("Row", row+1, [item.name for item in self.grid_items[row]])
