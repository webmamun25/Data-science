# function based on abstraction and decomposition

# create function

def is_even(num):
    """ this function given a number is odd or even """
    if(type(num)== int):

            if(num%2==0):
                return 'even'
            else:
                return 'odd'
    else:
        print('sudar ja')
for i in range(1,11):
    x=is_even(i)
    print(x)

# parameter vs argument

# function bananaor shmy j variable dei oita parameter
#
# function call korar shmy j variable dewa hoi oita argument
#
# games er shmy difficulty level parameter r point hosse argument

# types of arguments

# defaul argument

def power(a=1,b=1):
    return a**b
# power(2)
# power(2)

# positional argument
# a=2,b=3
power(2,3)

# keyword argument
# *args and **kward
power(b=3,a=2) #jeikane b ase sheikane b er man boshe jabe

# args and kwargs python keyword that are used to pass the variable
# issamotho argmuent pass kora jabe
def multiply(*args):
    product=1
    for i in args:
        product=product*i
    print(args) #found an tuple
    return product
multiply(2,3,4,5,5,56)

# docstring search
print(is_even.__doc__)


# **kwargs key value pair

def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key,'->',value)

display(india='delhi',srilanka='katmandu')


# point to remember while using args and kwargs

# order of the argument matters(normal->args->kwargs)
# the word args and kwargs are only a convention you can use any name of your choice

# how function executed in memory
# function er block scope er lifetime hosse call kora r return korar moddoborthi shmy porjontho take er por vanish hoi jai



# without return statement
# default return is None
L=[1,2,3]
print(L.append(4))
print(L)

# global variable vs local variable

def g(y):
    # y is local variable
    print(x)
    print(x+1)
x=5 #global variable
g(x)
print(x)  #answer is 5 6 5


def f(y):
    x=1
    x+=1
    print(x)

x=5
f(x)
print(x)


# locally used global variable but not change it thats why it shows error
def h(y):
    x+=1
x=5
h(x)
print(x)

# use global

def h(y):
    global x
    x+=1
x=5
h(x)
print(x)


# nested function

def f():
    def g():
        print('inside function g')
    g()
    print("inside function f")
f()

# 1st class citizen

def square(num):
    return num**2

type(square)
a=2
type(a)
id(a)
id(square)
# function in a python is a data type
# reassign
x=square
print(x)
id(x)
print(x(3))

# deleting a funciton
del square

# storing
L=[1,2,3,square]
L[-1](3)

# funciton is immutable data type

# function weired behavior

def f():
    def x(a,b):
        return a+b
    return x

val=f()(3,4)
print(val)

# function argument

def func_a():
    print('inside function')

def func_b(z):
    print('inside funciton c')
    return z()

print(func_b(func_a))

# benefit of using a funciton
# code modularity,code readability,code reusability

# lambda function
# lamda a,b:a+b
# x=>x^2

a=lambda x:x^2
a(2)

# x,y=>x+y
a=lambda x,y:x+y
a(2,3)

# diff between lambda vs normal funciton

# no name,lambda has no return value
# lambda written in 1 line not reusable

a=lambda s:'a' is s
a('hello')

a=lambda x:'even' if x%2==0 else 'odd'
a(6)

# higher order funtion
# return as a function or recieve a function

def square(x):
    return x**2
def transform(f,L):
    output=[]
    for i in L:
        output.append(f(i))
    print(output)
L=[1,2,34,4]

transform(square,L)
# alternative

def transform(f,L):
    output=[]
    for i in L:
        output.append(f(i))
    print(output)
L=[1,2,34,4]

transform(lambda x:x**2,L)


# map
L=[1,2,3,4]
print(list(map(lambda x:x**3,L)))

list(map(lambda x:'even' if x%2==0 else "odd",L))

users=[

    {
        'name':'rahul',
        'age':45
    },
        {
        'name':'rah',
        'age':65
    },{
        'name':'rahula',
        'age':35
    },

]

list(map(lambda users:users['name'],users))

# filter

l=[1,2,4,5,3,7,8]

list(filter(lambda x:x>5,l))

fruits=['apple','guaba']
list(filter(lambda x:x.startswith('a'),fruits))

# reduce

import  functools

functools.reduce(lambda x,y:x+y,[1,2,3,4,5])

functools.reduce(lambda x,y:x if x<y else y,[23,12,45,66,34])