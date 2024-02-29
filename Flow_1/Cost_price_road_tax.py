"""
Write a program to acces cost price of the bike and display the road tax to be paid according to the:
    Cost Price(in Rs)       Tax
    > 100000                15%
    >50000 and < 100000     10%
    <= 50000                5%
"""

bike_price = (int)(input("Enter the bike price: "))
tax = 0
if bike_price > 100000:
     tax = 15/100 * bike_price
     #print(tax)
elif bike_price >= 50000 and bike_price <= 100000:
    tax = 10/100 * bike_price
    #print(tax)
elif bike_price <= 50000:
    tax = 5/100 * bike_price
    #print(tax)
else:
    print("tax not applicable..")
print("tax to be paid: ",tax)


