# write a program to with for basic ATM machime operation

import time
print("Insert Card..\n")
print("wait for for validating card information....")
time.sleep(2)

pin = (int)(input("Enter four digit cad PIN: "))
amount = (int)(input("Enter the amount: "))

if amount >= 10000:
    print("more than 10000 amount not applicable.")
elif len(pin) == 4 and type(amount) == int:
    print("Cash Withdrow")

else:
    print("transaction failed..")



