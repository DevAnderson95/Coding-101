seats = input("How many people do you need a table for? ")
seats = int(seats)

if seats >= 8:
    print("Just a moment, we are waiting for an opening for this sized party. ")
else:
    print("Great, follow me this way. We have a table with " + str(seats) + " seats available" + "!")