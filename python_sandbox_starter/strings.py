# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Nijam'
age = 23

print("hello my name is "+name+" and i am "+str(age))   #Cannot connect non string inside

# String Formatting
print('My name is {name} and I am {age}'.format(name=name, age=age))
print(f'Hi, I am {name}, {age}')                        #Only in python 3.6++

# String Methods

s = 'hello world'
print(s.capitalize())
