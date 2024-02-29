
# Program to add and display the sum of n number of integer
def add(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:", sum)

add(2,6)
add(3,4,5,6,7)
add(1,2,3,5,6,7,8)