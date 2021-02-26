mystring = "Hello World"
print(mystring)
print(mystring[-1])
print(mystring[2:5])
s1 = "Vishwakarma " 
s2 ="Shivam"
print(s1 + s2)

#iterating through String

count =0
for l in "Hello World":
    if l=='o':
        count+=1
print(count , "Letter Found")

#using simple iteration and range()
#code1
String = "Gekksforgeeks"
#iterate through strings
for element in String:
    print(element ,  end ='')
print("\n")

#code2

StringName = "GEKKSFORGEEKS"
#Iterate over indexed

for element in range(0 ,len(StringName)):
    print(StringName[element])

 #Iterarte over reverse 
for c in StringName[::-1]:
    print(c , end = ' ')
    
    for c in reversed(StringName):
        print(c , end = ' ')
 
   

 
 