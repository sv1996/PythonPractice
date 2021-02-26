s ={1,2,3}  #sets of integers 
print(s)
print(type(s))
# set don't allow duplicates 
s= {1,2,3,1,4}
print(s) #prints only single value not duplicates 
s=set([1,2,3,4,1])
print(s)
#initialize a set with set() method 
s =set()
print(type(s))

# add element to a set 
s={1,2}
s.add(3)
print(s)
#add multiple elements to a set
s.update([5,6,1])
print(s)
#add list and set 
s.update([8,9] , {10,2,3})
print(s)