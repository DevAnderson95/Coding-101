my_dict = {
    1:'stability',
    2:'success',
    3:'peace',
    4:'prosperity',
    5:'health',
    6:'happiness',
}
my_dict[7] = 'longevity'

print(my_dict[2].title())
print(my_dict[7])
my_dict[6] = 'legacy'
print(my_dict)
my_dict[8] = 'progress'
print(my_dict)
#x = my_dict.get(2)
#print(x)
for key,value in my_dict.items():
    print(f'The Key is {key}')
    print(f'And this is the Value: {value.title()}')
#the (for key, value) function will retuurn your dictionary in an ordered manner with the assigned statement/code you choose
for key in my_dict.keys():
    print(key)
#the (for key) function will return all of your assigned keys in your dictionary
for value in my_dict.values():
    print(value.title())
#the (for value) function will do the same as the (for key) function it willreturn all values in your dictionary
##k,v can and will be used in multiple codes remember k is key and v is value  