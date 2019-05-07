# If/ Else conditions are used to decide to do something based on something being true or false
    #Same as others
x = 4
y = 5

if x > y:
    print('yes')
elif x == y:
    print('equal')    
else:
    print('no')


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
    #Same as others


# Logical operators (and, or, not) - Used to combine conditional statements

if x > 2 and x < 10:
    print('success')

if not(x == 14):
    print(f'{x} != 14')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

if x in numbers:
    print('in list')


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
