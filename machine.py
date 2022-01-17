# pylint: disable=C0114, C0115, C0116

from item import Item


class Machine:
    def __init__(self, columns: int, rows: int) -> None:
        self.list_items = [[0] * columns for i in range(rows)]
        self.columns = columns
        self.rows = rows

    def add_item(self, name: str, number: str, column: int, row: int):
        self.list_items[row-1][column-1] = Item(name, number, column, row)

    def remove_item(self, item):
        self.list_items.remove(item)

    def print_all(self):
        for row in range(self.rows):
            print("Row", row+1, [item.name for item in self.list_items[row]])
