grocery_list = ['meats','rice','beans','corn','milk',]
my_enumeration_station = list(enumerate(grocery_list))
print(my_enumeration_station)
[(0, 'meats'), (1, 'rice'), (2, 'beans'), (3, 'corn'), (4, 'milk')]
#list(enumerate) is to display the items  your list in numerical index order  
print(type(my_enumeration_station))
#(type) will define the class of your code (tuple,list,str,int)
my_tup = ('devon jr', 2)
print(my_tup[0].title())
#once put in a code a tuple cannot be changed 

print(my_tup[0])
nums_list = [1,1,1,2,2,2,3,6,7,8,9,10,10000000,5000]
print(nums_list)
my_tup = ('amanda',32)
nums_set_from_list = set(nums_list)
print(nums_set_from_list)
print(type(nums_set_from_list))
#(set) function will generate your list removing any duplicates
#in order to change a tuple you must copy it and add the change you want to make in the new definition 
new_tup = (my_tup[0], my_tup[1])
print(new_tup)
#you are basically overriding your old tuple to create a new definition 
