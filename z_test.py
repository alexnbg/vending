from funds import FundsControl
from money import Money

a = Money(10,10,10,10,10)

t = FundsControl(a)
print('t', t.get_balance())

cus = Money(0,0,0,0,1)
print ('insert', cus.balance)

p = 300
print('price', p)

ch = t.transaction(cus, p)

if ch:
    print('bal-', t.get_balance(), 'ch-', ch.balance)
else:
    print('bal-', t.get_balance())