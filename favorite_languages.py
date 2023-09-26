favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil':'python',
    }
print("Sarah's favorite language is " + favorite_languages['sarah'].title())

for name,language in favorite_languages.items():
    print(name.title() + "s" + " favorite language is " + language.title())
for name in favorite_languages.keys():
    print(name.title())
#you can loop through a dictionary easily using the (for) statement and selecting which keys you would like to show 
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hello " + name.title() + ", I see you favorite language is " + favorite_languages[name].title() + ".")
#    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll")
 #you can check to see if an item/name is in your dictionary keys by using the (if) statement for keys       
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", Thank you for taking our poll!")
#you can sort through your dictionary by using the(sorted) function 
print("The following languages have been mentioned, ")
for language in set(favorite_languages.values()):
    print(language.title())
#using a (set) function can make sure that your code output does not repeat itself even if the dictionary has multiple pieces of one particular item stored 
