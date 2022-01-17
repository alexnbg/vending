# pylint: disable=C0114, C0115, C0116

from money import Money

class FundsControl:
    def __init__(self, money: Money) -> None:
        self.money = money

    def get_balance(self):
        return self.money.balance

    def transaction(self, amount:Money, price_st:int):
        """
        Makes the transaction and returns the change as Money object.
        Returns False if the inserted amount is less than the price
        or there are no money to return change
        """
        diff = amount.balance - price_st
        change = Money(0, 0, 0, 0, 0)

        if diff == 0:
            return change
        elif diff > 0:
            while diff >= 200:
                diff -= 200
                change.st_200 += 1
            while diff >= 100:
                diff -= 100
                change.st_100 +=1
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
            else:
                self.money = self.money + amount
                self.money = self.money - change
                return change
        else:
            return False
    
        






