my_person = {
    'first name':'amanda',
    'last name':'rosado',
    'age':32, 
    'dob':'August,10,1991',
    'kids':'mother of one',
    'city':'yonkers',
    'sons name':'devon michael anderson jr',       
             }
print("My fiancee's name is " + my_person['first name'].title() + " " + my_person['last name'].title())
print(my_person['first name'].title() + " was  born " + my_person['dob'] + ".")
print(my_person['first name'].title() + " is a " + my_person['kids'] + "." +
      "\nHer first born child is named " + my_person['sons name'].title())
print("She was born and for the most part raised in the city of " + my_person['city'].title() + ".")
print("This year " +my_person['first name'].title() + " turned " + str(my_person['age']) + " years old" + "!")