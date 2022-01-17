# pylint: disable=C0114, C0115, C0116
class Item:
    def __init__(self, name: str, number: str, price:int, column: int, row: int) -> None:
        self.name = name
        self.number = number
        self.price = price
        self.column = column
        self.row = row

    def get_location(self):
        return {'column': self.column, 'row': self.row}

    def remove_item(self, number=1):
        self.number = self.number - number
