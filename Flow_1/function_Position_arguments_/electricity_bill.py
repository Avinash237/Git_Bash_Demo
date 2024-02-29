# program to pritnt/accept correct eletricity bill information

def electricity_bill(unit,rate):
    price = unit*rate
    return price

bill = (electricity_bill(100,18))
print(bill)

bill2 = electricity_bill(96,101)   # wrong parameter
print(bill2)

