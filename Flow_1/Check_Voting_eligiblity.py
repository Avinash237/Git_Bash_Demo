# write a program to check person is eligible or not for voting

person_age = (int)(input("Enter The Person Age: "))

if person_age == 0:
    print("Not Eliglible peson...")
elif person_age >= 18:
    print("eligible for voting....")
else:
    print("you age is not eligible for voting.")
