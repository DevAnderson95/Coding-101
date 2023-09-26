#make an empty list for aliens 
aliens = []

#make 30 green aliens 
for alien_number in range(30):
    new_alien = {'color':'green','points': 5,'speed':'slow'}
    aliens.append(new_alien)

#show the first 5 aliens
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


for alien in aliens[0:5]:
    print(alien)



print("...")

#show how many aliens have been created 
print("Total number of aliens " + str(len(aliens)))