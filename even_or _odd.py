number = input("Tell me a number and ill tell you if its evrn or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.") 
else:
    print("\nThe number " + str(number) + " is odd.")