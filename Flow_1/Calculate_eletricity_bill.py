"""Write a program to calculate the eletricity bill (Accept number of unit from user)
   according to the following criteria:

   unit                     price
  first 100 unit          no charge
  Next 100 unit           rs 5 per unit
  after 200 unit          rs 10 per unit

"""
meter_unit = (int)(input("Enter the unit: "))

if meter_unit <= 100:
    print("Not extra charges aplicable.")
elif meter_unit > 100:
    print("your bill amount:",meter_unit * 5)
elif meter_unit >= 200:
    print("your bill amount:",meter_unit * 10)
else:
    print("wait for next bill....")
