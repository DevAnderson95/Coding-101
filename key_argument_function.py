def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first 
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
#alwyas include an empty dictiobnary to include your list in a function 
#using the ** for user info allows other information and key values to be stored in the function 
user_profile = build_profile('albert','einstein',
                             location = 'princeton',
                             field = 'physics')

print(user_profile)
