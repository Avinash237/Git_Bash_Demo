# write a program to check entered year is leap year or not

year = (int)(input("enter the year: "))

if year%100 == 0:
    if year%400 == 0:
        print("Enter year is leap year..!")
    else:
        print("Enter year is not leap year.")
else:
    if year%4 == 0:
        print("Enter year is leap year...!")
    else:
        print("Enter year is not leap year.")





