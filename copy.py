#copying a list can be used to store the list in your program and run it again when needed
my_foods = ['hamburger','pizza','shrimp','tacos','ice cream']
amandas_foods = my_foods[:]
print("My Favorite foods:")
print(my_foods)
print("\n" + "Amandas Favorite foods:") 
print(amandas_foods[2:5])
#copying a list consist of making an original list and then making another name for the list with a different title(string)
my_foods.append('lobster')
print(my_foods)
amandas_foods.append('guacamole')
print(amandas_foods)
my_foods.append('steak')
amandas_foods = my_foods[3:7]
print(my_foods)
print(amandas_foods)
amandas_foods.append('guacamole')
print(amandas_foods)
#this shouldnt workk 
amandas_foods = my_foods
print(amandas_foods)
my_foods.append('mango')
print(my_foods)
print(amandas_foods)
amandas_foods.append('grapes')
print(my_foods)
print(amandas_foods)
#if you equal the list to the new title(string) you will not have copied the list you musyt always use[:]