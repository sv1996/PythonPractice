from functools import reduce
lst =[1,2,3,4,5,5]
def multiply(x ,y):
    return x*y


product = reduce(multiply , lst)
print(product)