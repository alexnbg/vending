# pylint: disable=C0114, C0115, C0116, R0913

class Money:
    def __init__(self,
                 st_10: int,
                 st_20: int,
                 st_50: int,
                 st_100: int,
                 st_200: int
                 ) -> None:
        self.st_10 = st_10
        self.st_20 = st_20
        self.st_50 = st_50
        self.st_100 = st_100
        self.st_200 = st_200

    def __add__(self, other):
        return Money(
            self.st_10 + other.st_10,
            self.st_20 + other.st_20,
            self.st_50 + other.st_50,
            self.st_100 + other.st_100,
            self.st_200 + other.st_200
        )

    def __sub__(self, other):
        return Money(
            self.st_10 - other.st_10,
            self.st_20 - other.st_20,
            self.st_50 - other.st_50,
            self.st_100 - other.st_100,
            self.st_200 - other.st_200
        )

    def __ge__(self, other):
        return all([
            self.st_10 >= other.st_10,
            self.st_20 >= other.st_20,
            self.st_50 >= other.st_50,
            self.st_100 >= other.st_100,
            self.st_200 >= other.st_200
        ])

    @property
    def balance(self):
        balance = (self.st_10*10
                   + self.st_20*20
                   + self.st_50*50
                   + self.st_100*100
                   + self.st_200*200)
        return balance
