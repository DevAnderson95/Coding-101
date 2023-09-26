players = ['dollaz','top','notch','shady','spice','sugar']
print(players[0:3])
#another way to generate multiple items from your list is the slice(:) fuction
#ex list = [1,2,3] 
#print(list[0;3])
print(players[:3])
#print(list[:3]) will generate every item in your list from the beginning 
#this is because you have stopped the funtion from targeting an item by omitting the list 
print(players[2:5])
#you can also target where you would like your list to start from by selecting the index number 
print(players[2:])
print("These are the first 3 players on my team:")
for player in players[:3]:
    print(player.title())
print(player)

