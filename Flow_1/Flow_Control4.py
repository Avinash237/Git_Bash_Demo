"""
Flow controll block:
3. Transfer statment:
    - break
    - continue
    - pass
All are kaywords use for specific purpose
"""
# break: to exit from current execution if condition gets satisfied
"""
num = [10,20,40,-1,60.77,84,-20,99]
#stop if we get -ve number
for i in num:
    if i <=0:
        break
    else:
        print(i)

-------------------------------------------------------------
# stop if age< 20
age = 11
if age < 20:
    break    # error
else:
    print("age")
 # we can only use break/contunue inside for/while loop
 
-----------------------------------------------------------------

# continue staement 
num = [10,20,-1,30,44,-20,88,44]
# skip the -ve number
for i in num:
    if i < 0:
        continue
    else:
        print(i)
        
-------------------------------------------------------------


cart = [499,800,2900,1999,199,599,99,700,100,500]
# skip item below 500 and print the total bill

f = []
for item in cart:
    if item<500:
        continue
    else:
        print("Item price",item)
        f.append(item)
print("Tital item selected: ",len(f))
print("Total bill: ",sum(f))
----------------------------------------------------------------

for i in range(6):
    if i==3:
        break
        #continue
    else:
        print(i)
-----------------------------------------------------------------

pass is used to create empty block

for i in range(4):
    pass
"""