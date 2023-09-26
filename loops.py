available_toppings = ['pepperoni','anchovies','sausages','extra cheese','buffalo ranch','olives','mushrooms']

#counter = 0 
#letter_to_check = input("what letter should we check here?")
for item in available_toppings:    if item[0] == letter_to_check:
        print(item)
else:
    print("This does not have that letter")
counter += 1 
print(counter)

toppings_length = len(available_toppings)
print(toppings_length)
#there are many ways to check your list for specifics using "letter to check" or "dooes not start with "