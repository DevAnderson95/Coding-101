my_dict = {
    'basketball':['new york knicks','miami heat','la lakers','golden state'],
    'football':{'nfl':['giants','jets','grizzlies','ravens'],
                'college':['clemson','UCLA','alabama']},
    'baseball':{'yankees','mets','red sox','pirates'},

}
print(my_dict['football']['nfl'][1].title())
print(my_dict['basketball'][2].upper())
print(isinstance(my_dict['basketball'][1], str))
#(isinstance) can be used as a boolean to returnn a true or false statement
print(isinstance("hello world", str))