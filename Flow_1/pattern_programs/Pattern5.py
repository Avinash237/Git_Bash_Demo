"""
      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *
* * * * * * *

"""
print("print equilateral triangle pyramid using star")
size = 7
m = (2 * size) - 2
for i in range(0,size):
    for j in range(0,m):
        print(end=" ")
    m = m - 1 # derementing m aftereach loop
    for j in range(0,i + 1):
        # printting full triangle pyramid using star
        print("* ",end=' ')
    print(" ")
