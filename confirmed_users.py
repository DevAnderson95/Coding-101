#start with users that need to be verified 
#and make an empty list to hold the confirmed users 

unconfirmed_users = ['amanda', 'devon','devon jr']
confirmed_users = []

#Verify each user until there are no more unconfirmed users 
#move each user into the list of confirmed users 

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
#display all confirmed users
print("\nThe following users have been confirmed: ") 
for confirmed_user in confirmed_users:
    print(confirmed_user.title())