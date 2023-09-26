#the if statement defines the truth of your variable(int)
x = 122
#BOOLEAN
y = False 
z = True 
if y:
    print("x is big")
    print("look here")
elif x == 10:
    print("x is 10")
#elif is short for else if and can also  be used as the else statement
else:
    print("x is tiny")
#the (else) function states that if the code is not true the another code can be generated otherwise 
#more list stuff 
#[start:end;stop]
my_list = ['food','cars','business','luxury','mansion']
print(my_list[0::1])
#the (::) function in slice can allow you to jump through your list to your liking in matter of spaces (ex print(my_list)[0::2])
print(f'I want to own a {my_list[2]} one day to change the world!')
#when using  a list you can use (print(f"add yur statememt or code " {my_list{item writin as {}}))