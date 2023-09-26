prompt = "\nPlease provide your age for ticket pricing: "
age = input(prompt)
flag = True

    

    


while flag:
    if age.lower().strip() == 'quit':
        break 
    
    elif int(age) <= 3:
        print("\nYour ticket is Free! Enjoy! ")
        
    elif int(age) <= 12:
        print("\nYour ticket is $10! Enjoy! ")
        
    else:
        print("\nYour ticket is $15! Enjoy") 
         

    age = input(prompt)
    


    