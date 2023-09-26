responses = {}

#set flag to indicate that polling is active
polling_active = True 

while polling_active == True:
#prompt the persons name and response 
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb one day? ")

#store the reponses in a dictionary 
    responses[name] = response 

#Find out if anyone else would like to take the poll 
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False 

#polling is complete show the results 

print("\n---Polling Results---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
