available_toppings = ['pepperoni','anchovies','sausages','extra cheese','buffalo ranch','olives','mushrooms']

urgent_toppings = []
for item in available_toppings:
    if item[0] in ['a','b','c']:
        urgent_toppings.append(item)
    else:
        continue
print(urgent_toppings)
my_toppings = [item for item in urgent_toppings if item[0] in ['a','b','c']]
print(my_toppings)
#you can shorten your code by defining the item specifically and determing which items you want pulled from your list 
for i in available_toppings:
    print(i)
    pass


