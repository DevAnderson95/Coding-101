def make_shirt(shirt_size, message= 'i love python'):
    """Display information about """
    print("\nThis is a "  + shirt_size + " T-shirt.")
    print("The shirt says " + message.title())

make_shirt('small', 'success is key!!!')
make_shirt('medium', 'make a change for the greater good!')
make_shirt('large', 'lead by example!')
make_shirt(shirt_size= 'small', message= 'success is key!!!')
make_shirt(shirt_size= 'medium', message= 'make a chamge for the greater good!')
make_shirt(shirt_size= 'large', message= 'lead by example!')
make_shirt('large')
make_shirt('medium')
make_shirt('small','give it all you got!')
