def build_person(first_name, last_name, age=' ', height=' '):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age 
    elif height:
        person['height'] = height 
    return person 

musician = build_person('jimi','hendrix',age = 27)
print(musician)
my_player = build_person('devon','anderson',age = 28,height = 5-7)
print(my_player)