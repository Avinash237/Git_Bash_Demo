"""
Accept the following from the user and calculate the percentage of class attend
    - Total number of working days
    - Total numer of days of absent

    After cllculating percentage show that, if the percentage is less taan 75, the student willnot able to sit in exam
"""

working_days = (int)(input("Enter the total number of working days: "))
absent_days = (int)(input("Enter the total number of absent days: "))

per = (working_days-absent_days)/working_days * 100
print("your attendence is",per)
if per < 75:
    print("Your are not eligible for exam.")
else:
    print("You are eligible for exam.")