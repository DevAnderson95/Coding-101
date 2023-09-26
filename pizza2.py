prompt = "\nWhat would you like on your pizza? "
prompt += "\n(Enter 'quit' when you are finished.) "

toppings = " "

while True:
    toppings = input(prompt)
    
    if toppings == 'quit':
        break
    else:
        print("Adding " + toppings.title() + " to your pizza.") 
    



    
    




