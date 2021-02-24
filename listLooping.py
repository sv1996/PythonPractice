lst = ['one' , 'two' ,'three' ,'four']
for ele in lst:
    print(ele)

    #list comprehension
    square =[]
    for i in range (10):
         square.append(i**2 )
    print(square)
    # with List comprehension
    square =[i**2 for i in range(10)]
    print(square)
