number =[3,1,5,12,8,0]
sorted_list =sorted(number)
print("Sorted list is " , sorted_list)
#original lst remain unhanged
print("Original list is " , number)

# print list in reverse order
print("Reverse soretd list is " , sorted(number , reverse =True))
#original list remain unchanged
print("Original list is " , number)

#sort the list within itself 
lst =[1,20,5.5,4.2]
lst.sort()
print("Sorted list is" , lst)

lst =[1,2,3,4,5]
abc = lst
abc.append(6)
#print original list
print("Original List is " , lst)
