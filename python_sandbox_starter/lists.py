# A List is a collection which is ordered and changeable. Allows duplicate members. Similar to array

#Create List
numbers = [1, 2, 3, 4, 5]
numbers2 = list((1, 2, 3, 4, 5))

#print(numbers, numbers2)

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#Choose Entry
print(fruits[1])

#Length of Array
print(len(fruits))

#Append to the end of the list
fruits.append('Mangos')
print(fruits)

#Change Value
fruits[0] = 'Blueberries'

#Remove stuff
fruits.remove('Grapes')

#Insert
fruits.insert(2, 'Strawberries')
print(fruits)

#Pop from list
fruits.pop(2)

#Reverse List
fruits.reverse()

#Sorting in alphabetical order
fruits.sort()


