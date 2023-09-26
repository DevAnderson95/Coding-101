prompt = "\nPlease enter the name of a city you have visted: "
prompt += "\n(Enter 'quit' when you are finished. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("\nI'd love to go to " + city.title() + "!")

#using the (break) function can exit out of a loop in a code when you need it to