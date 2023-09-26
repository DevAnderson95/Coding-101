
requested_toppings = ['pepperoni', 'sausage', 'bacon','buffalo ranch']

for requested_topping in requested_toppings:
    if requested_topping[1] == 'sausage':
        print("Sorry, we are currently out of sausage toppings at the moment.")
else:
        print("\nAdding " + requested_topping + ".")

print("\nFinishing your Pizza!")
#adding an (if) statement when making a selective list for orders,options,etc. can single out an item in your list 
#ex: if sausage is not available add (if) statement to your for statement and to single out the item and add the (else) statement for the rest of your items to be presented  