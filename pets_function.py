#positional arguments 
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet('dog','mamas')
#describe_pet('cat', 'blue')

#Keyword Arguments do not have to be in any order as long as you have the paramters inside the function 
#be sure to use the exact names of the paramaters in the function
#describe_pet(pet_name = 'mamas', animal_type = 'dog')
#describe_pet(animal_type = 'dog', pet_name = 'mamas') 
#Default values can be used to simplify a function call by setting the value in the parameters of the function 
#When using deafult values the parameter containing the value must be placed at the end of the function while any parameter that does not have a positional argument should be placed first 
describe_pet('mamas')
#to change the argument if a default value is set you can redefine the function by including two new arguments  
#all of the functions called below can be used 
describe_pet(pet_name= 'blue', animal_type= 'cat')
describe_pet('whiskers', 'cat')
describe_pet('brownie')
describe_pet('sleek', 'lizard')
#always include an argument in a function call to avoid argument errors 
#describe_pet()