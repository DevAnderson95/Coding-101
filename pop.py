#the #(pop) method lets you remove the last item from a list but still hold its place
cars = ['chevy', 'honda', 'nissan', 'toyota']
print(cars)
popped_cars = cars.pop()
print(popped_cars)
numerous_owned = cars[1]
message = "I have never owned a " + popped_cars + " before" + "."
print(message)
message = "I have owned a " + numerous_owned + " twice" + "."
print(message)
#you can use the pop() method for many different ways to change your text or program 