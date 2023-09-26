alien_colors = ['red', 'green','blue']
 
if 'green' in alien_colors:
    print("You earned 10 points!")
if 'blue' in alien_colors:
    print("You earned 25 Points")
if 'red' in alien_colors: 
    print("You earned 50 points!")

print("\n CONGRATS YOU WIN!!!")

if 'brown' in alien_colors:
    print("Try again")

alien_colors.append('yellow')

if 'yellow' in alien_colors:
    print("You earned 100 points!")
elif 'yellow' not in alien_colors:
    print("try again")

if 'brown' in alien_colors:
    print("YOU LOSE!")
elif 'brown' not in alien_colors:
    print("Job Well Done!")

