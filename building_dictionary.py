alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
#you can create a dictionary and singley add different keys if its easier for you 
#modifying a dictionary can simply be done by taking your key and changing the variable 
alien_0['color'] = 'yellow'
print("The alien color is now " + alien_0['color'] + ".")
alien_0 = {'x_position':0, 'y_position':25, 'speed': 'medium'}
print("Original x position: " + str(alien_0['x_position']))

#Move the alien to the rightt 
#dDetermine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1 
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3 

#the new position is the old position plus the increment 
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x_position: " + str(alien_0['x_position']))
#you can remove an item in you rdictionary by using the (del) function 
