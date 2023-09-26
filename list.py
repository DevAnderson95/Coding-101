family = ['Devon Sr.', 'Amanda', 'Devon Jr']
print(family)
print(family[0])
print(family[1])
print(family[2])
#print(subject[]) with a num. is to singly print out a variable from your list 
print(family[-1])
#[-1] is to always generate the last variable on your list 
message = "My pride and joy is " + str(family[2]) + "."
print(message) 
#to add a period to your printed messsage with a list "."
wants = ['tesla', 'range rover', 'ferarri', 'house', 'business'] 
message = "I want to own a " + wants[1].title() + " one day" + "."
print(message)
#when creating statements with your list always add a space after the last text to ensure your statement is is readable 
#this also goes for continuing a sentence with a [single] or multiple choices from your list
wants[0] = 'corvette'
print(wants)
print(message)
message = "I want to own a " + wants[0].title() + " one day" + "."
print(message)
#to change the a specific value in your list selct the [] number in the order yoour list goes and replace it with a different value 
wants.append('lotus')
print(wants)
#appending and item is to add a value to your list in your program 
#you ccan also create a list from scracth by appending a variable ex: wants.append('mansion') 
wants.append('mansion')
message = "I want to own a " + wants[6].title() + " one day, its always been my dream" + "."
print(message)
#you can also delete an item or items by using the #del item [1,2,3] syntax from your list 
#once #del is used you no longer have access to the item in your list 
#when using pop() method the item you have used it on is no longer stored and must me added back ("append")