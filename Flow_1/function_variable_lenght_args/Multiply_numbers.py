






def multiplyNumbers(*numbers):
    product = 1
    for n in numbers:
        product *= n
    return product


print("product:", multiplyNumbers(4, 4, 4, 4, 4, 4))