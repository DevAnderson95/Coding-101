available_toppings = ['pepperoni','anchovies','sausages','extra cheese','buffalo ranch','olives','mushrooms']
requested_toppings = ['pepperoni','anchovies','extra cheese','mushrooms','french fries']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping.title() + ".")
    else:
        print("Sorry we are out of " + requested_topping + ".")

print("\nFinishing your pizza!")
print
#you can create multiple list in a code and sort through the list using the (for) function 


    