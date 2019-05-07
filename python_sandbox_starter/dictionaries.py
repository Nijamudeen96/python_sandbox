# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Create dict
person = {
    'first_name': 'John',
    'last_name' : 'Doe',
    'age': 32
}

print(person, type(person))
print(person.get('first_name'))

#Add key/value
person['phone'] = '555-5555-555'

#Get keys
print(person.keys())
print(person.items())

#Copy Dictionary
person2 = person.copy()
person2['city'] = 'Singapore'

#Remove item
del(person['age'])
person.pop('phone')

#Clear
person.clear()

#Length
print(len(person))

#List of dictionary
People = [
    {'name': 'Martha', 'age': 30},  
    {'name': 'Jack', 'age': 45}
]