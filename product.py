lst = [10 ,20, 30 ,40,50]
product =1
index=0
while index < len(lst):
    product *= lst[index]
    index+=1

print("product is {}" .format(product))