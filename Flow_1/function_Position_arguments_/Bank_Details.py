


def Bank_Detils(name,branch,IFSC,PIN):
    return name,branch,IFSC,PIN

name = input("Enter the bank name: ")
branch = input("Enter the Branch name: ")
IFSC = int(input("Enter the IFSC Code: "))
PIN = int(input("Enter the bank PIN: "))

Bank_Detils(name,branch,IFSC,PIN)
