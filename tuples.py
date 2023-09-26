
# Python refers to values that cannot change as immutable, and an immutable list is called a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print(dimensions)
for dimension in dimensions:
    print(dimension)

#writing over a tuple
dimension = (200,50)
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified Dimensions:" )
for dimension in dimensions:
    print(dimension)

#The block atudefines the original tuple and prints the initial dimen- sions. Atv, we store a new tuple in the variable dimensions. We then print the new dimensions atw. Python doesn’t raise any errors this time, because overwriting a variable is valid:
#always remember to use a tuple only when you want to store a variable/list to use later in your code(program)