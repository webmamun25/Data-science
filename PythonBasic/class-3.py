# strings

# strings are sequence of unicode character

# create strings

s='hello'
print(s)

s="hello"
s='''
multiple line strings

'''
# two comma together
s="it's raining outside"

s=str('Hello')

# accesing substring

s=" hello world"

# positive indexing

print(s[0])

# negative indexing
print(s[-1])

# slicing
print(s[1:6])
print(s[2:3])
print(s[1:])
print(s[:4])
print(s[:])
print(s[0:6:3])
print(s[6:0:-1])
print(s[::-1]) #reverse string
print(s[-5:])
print(s[-1:-6:-1])

# editing deleting
s[0]='H'  #immutable

del s
print(s)
del s[-1:-5:-2] # throw an error because partial deletion is not allowed


# operator work in string

# arithmetic operator
print('delhi'+" "+'mumbai')
print("delhi"*5)
# subtraction and deletion not work

# relational operator
'delhi'=='mumbai'
'mumbai'>'pune'
# lexiographicaly compare which word come first is lowest and which come tolast it is bigger than the other one
# 'Phune'>'phune'
# ascii value 50>112 so false

# logical operator

'hello' and 'world'
# answer is world
'hello' or 'world'

# in python '' empty string is false and 'h' contains any value means true
'' and 'world' # answer is ''
'' or 'world' # answer is 'world'
not 'hello' #answer is false

for i in 'hello':
    print(i)

'd' in 'Delhi' # case sensetive


# string function

# common function
# len max min sorted all are common for any data type

len('hello world')
max('hello world')
min('hello world')
sorted('hello world',reverse=True) #output is list

# only string function
s="hello world"
s.capitalize()
s.title()
s.upper()
s.lower()
'HellowOrld'.swapcase()

# count find index

'my name is mamun'.count('a')

'my name is mamun'.find('is')
'my name is mamun'.find('x') #return -1

'my name is mamun'.index('is')
'my name is mamun'.index('x') #throw error

'my name is mamun'.endswith('un')
'my name is mamun'.startswith('my')

# string formating
name='nitish'
gender='male'

'hi my name is {} and i am a {}'.format(name,gender)

# isalpha/isdigit

'nitish1234%'.isalnum() #check alphanumeric

'nitish'.isalpha()

'123abc'.isdigit()
'first_name'.isidentifier()

# split/join

'hi name is kareena'.split()
' '.join(['hi','my'])
"hi name is kareena".replace('kareena','campusx')

"   hi a sdmfksf ".strip()

