#.remove() can be used to also alter\remove an item from your list but still hold its value 
cars = ['chevy','honda','nissan', 'tesla']
print(cars)
cars.remove('tesla')
print(cars)
#you can also define the item removed and use it as a reason in a text in a message of a program 
cars = ['chevy','honda','nissan','maserati']
print(cars)
very_expensive = 'maserati'
print(cars.remove(very_expensive))
print("\nA " + very_expensive.title() + " is a very expensive for me" + "." ) 
#("\nA" + item_removed ) can single out and explain the selected removed item 