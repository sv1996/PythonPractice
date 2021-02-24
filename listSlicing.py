number =[10,20,30,40,50,60,70,80,90]
#print all numbers 
print(number[:])
print(number[0:4])
#print alternate numbers (start:end:steptaken)
print(number[::2])
print(number[2::2]) #start from 2 ind index and go to end with 2 steps 
# List extend using "+"
l1=[1,2,3,4]
l2 =['verma' , 'shivam' , 'karma']
new_list =l1+l2
print(new_list)

#list count (frequemcy)
number=[1,2,3,1,3,4,2,5]
#frequency of 1
print(number.count(1))
print(number.count(3))