numbers = [1,2,3,4 ,5 ,6]
def powerOfTwo(num):
    return num**2 

#using map() function 

squared = list(map(powerOfTwo , numbers))
print(squared)