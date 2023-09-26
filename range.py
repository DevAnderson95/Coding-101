numbers = ["1,2,3,4,5,6,7,8,9,10"]
print(numbers)
for value in range(1,5):
    print(value)
#the range() loop will generate multiple values in your list of numbers 
numbers = list(range(1,6))
print(numbers)
#list(range) will generate your numbers in the original list form but only the items you slected up to in your list 
even_numbers = list(range(1,11,2))
print(even_numbers)
#list(range) can also sort through the list and retrieve even or odd numbers by identifying the number differential at the end of the range()
print(min(numbers))
print(max(numbers))
print(sum(numbers))
#(min,max, and sum) functions allow you to figure out the lowest and maximum value of your list as well as the total sum of all the digits your list contains 
