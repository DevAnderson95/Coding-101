def greet_user():
    """Display a simple greeting."""
    print("Hello!")
#while (def) a function you must use a docstring(line 2) to define what the function is meant to do 
greet_user()
#(username) is the parameter in the function which is a piece of information the function needs to do its job in a program 
def greet_user2(username):
    """Display a simple greeting message."""
    print("Hello, " + username.title() + "!")

greet_user2('amanda')
#('amanda') would be the argument that is passed from a function call to a function
):