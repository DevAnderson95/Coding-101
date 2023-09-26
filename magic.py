family = ['amanda', 'devon jr', 'davion']
print(family)
for member in family:
    member = 'amanda'
#when using the for() loop in a list you must define the variable you are using with an item from your list 

print(member)
for member in family:
    member = 'devon jr'
#to change the item of the variable use the for() loop again redefininig the variable
print(member)
for member in family:
    member = "davion"

print(member.title())
print("Hey " + member.title() + ", how have you been?")



