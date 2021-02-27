# display fibonacci sequence up to nth term using recursive function call
def fibonacci(num):
    """ Recursie function to print fibonacci sequence

    """
    if(num<=1):
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
















nterms =10
print("Fibonacci sequence")
for num in range(nterms):
    print(fibonacci(num))



















