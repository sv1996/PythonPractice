my_dict = {}
#dictionary with integers keys and values

my_dict = {1:'abc' , 2 :'xyz'}
print(my_dict)

my_dict={'name' :'satish' , 1:['abc' , 'xyz']}
print(my_dict)

# create a empty dictionary using dict()

my_dict =dict()
my_dict = dict([(1,'abc') , (2 , 'xyz')])
# create a dictionary with list of tuples 

print(my_dict)

#dictionary acess
print(my_dict[1])
#delete in dictionary with

print(my_dict.pop('age',1))
print(my_dict)