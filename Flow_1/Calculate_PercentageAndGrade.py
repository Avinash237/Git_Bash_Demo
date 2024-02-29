"""write a program to accept percentage from the user and display the grade according to the following criteria:
    Marks           Grade
    >90                A
    >80 nd <=90         B
    >60 and <=80        C
    below 60            D
"""

per = (int)(input("Enter the marks: "))

if per >= 90:
    print("Grade A")
elif per >= 90 and per <=80:
    print("Grade B")
elif per >= 80 and per <=60:
    print("Grade C")
elif per >= 60 and per <=40:
    print("Grade D")
else:
    print("Failed....")

