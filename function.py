def print_name (name ):
    print("hello" , end =' ' + str(name))
    print(print_name.__doc__)



print_name("satish")

## function for sum iof list 

def get_sum(lst):
    #Initializing the sum
    sum=0
    #Iterating over the sum
    for num in lst:
        sum+=num
    return sum

s= get_sum([1,2,3,4,5])
print(s)

