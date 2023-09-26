def get_formatted_name(first_name, last_name, middle_name=' '):
    """Return a full name neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hemdrix')
print(musician)

musician =  get_formatted_name('john', 'hooker', 'lee')
print(musician)
#making an argument optional
#by putting middle_name at the end of your parameters and giving it a default value of ' ', we are giving the user an option 
#they can decide if they want to include a middle name without the code being interrupted
#in this sense you would have to provide the middle name last since it is last in the parameters 
 
