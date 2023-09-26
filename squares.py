squares = []
for value in range(1,21):
    square = value ** 2 
    squares.append(value ** 2)
print(squares)
#list_comprehension() can combine the values of a for loop in just one line of code 
squares = [value ** 2  for value in range(1,11)]
print(squares)

numbers = [value * 1 for value in range(1,1000001)]
print(numbers)