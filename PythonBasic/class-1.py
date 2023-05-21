"""print("hello",end=" ")
print("world")

1*10^308 handle integer in python
1*7^308 handle float type in python

print(True)
print(False)
print("Hello World")

print(5+6j)

print([1,2,3,4,5])
print((2,3,4,5,6))
print({1,2,3,4,5})
print({'name':'nitish','gender':'male'})

print(type(3.5))
print(type("hello"))"""


#Variables

name='nitish'
print(name)
a=5
b=6
print(a+b)

''' multiline comment '''


# user input
# take input from users and store them in a variable
#
# a=int(input("enter your number: "))
# b=int(input("enter your second "))
# add  2 variable
c=a+b
# print the result
# print(c)

# Type conversion

# implicit int and float
print(5+5.6)
# not possible
# print(4+'4')
# explicit
type(int('4'))
# not possible
# int(4+5j)


# Literal

a=2
# a is variable ,= is operator ,2 is literal
# binary
a=0b1010
# decimal
b=100
# octal
c=0o310
# hexa
d=0x12c
print(a)

x=3.14j
print(x.real)
print(x.imag)
a=True+4  # true mean 1
b=False+10 # false 0

a=None
print(a)
