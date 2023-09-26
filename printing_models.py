#Start with some designs that need to be printed 
unprinted_designs = ['iphone case', 'robot pendant', 'shirt design']
completed_models = []

#simulate printing each design until none are left
#move each design to completed models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #simulate creating a 3D print from the design.
    print("Printing model: " + current_design.title())
    completed_models.append(current_design)

#Display all complted models
print("\nThe following models have been completed: ")
for completed_model in completed_models:
    print(completed_model.title())