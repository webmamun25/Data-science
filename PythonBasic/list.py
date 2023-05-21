#list

# list is a data type where you can store multiple items under 1 name
l=[20,30,40]

# Array vs list
# fixed vs Dynamic size int arr[50] list=[]
# convenience>heterogenous arrays are homogenous but list is hetrogenous
# speed of execution array is faster
# memory array is less occupy memory

# how list stored in memory

# referential array

a=2
print(id(2))

L=[1,2,3]
print(id(L))
print(id(L[0]))
print(id(1))

# characteristic of list

# ordered
l1=[1,2,3]
l2=[3,2,1]
print(l1==l2)

# mutable

L=[]

# Heterogeneous

# item can be duplicate

# are dynamic

# can be nested
# item can be accessed
# can contain any kind of objects in python

# creating a list
# homogenous vs hetrogenous bujar upai hosse bairer bracket er modde same typer data thakle homo otherwise hetro
print([])
print([1,2,3]) #homogenous
print([1,2,3,[1,2,3]]) #hetrogeneous
print([[[2,4],[1,3]]]) #homogenous
print([1,2,True]) # hetrogeneous
print(list('hello'))

# accessing

List=[1,2,3,4,5]
print(List[0])
print(List[-1])
List2d=[1,2,3,[4,5]]
print(List2d[-1][-1])
# slicing

print(List[0:3])
print(List[-3:-1])

# adding items

Ladd=[1,2,3,4,5]
Ladd.append(5)
print(Ladd)

Ladd.extend([6,67,8])
print(Ladd)

Ladd.insert(2,[4,5])
print(Ladd)

# editing item

s=[1,2,3,4]
s[-1]=500
print(s)
s[1:4]=[20,33,44]
print(s)

# deleting item

s1=[12,3]
print(s1)
del s1
print(s1)

del s1[-1]
print(s1)

del s1[1:3]
print(s1)

L=[1,2,3,4,5]
L.remove(5)
print(L)

L.pop(0)
L.pop()
L.clear()
print(L)


# operation
# arithmetic +,*

L1=[1,2,3,4]
L2=[5,6,7,8]
print(L1+L2)
print(L1*3)

# membership
print(5 in L1)
# loop
for i in L1:
    print(i)

# function

len(L2)
min(L2)
max(L2)
sorted(L2)

L1.count(1)
L1.index(1)

L1.reverse()  #permanent operation

print(L1.sort) #permanent sort but sorted is temporary
# copy
L1.copy()
print(L1)


# list comprehension
# newlist=[expression for item in iterable if condition==True]

# add 1 to 10 numbers in list
l=[i for i in range(1,11)]

v=[2,3,4]
s=-3
x=[i*s for i in v]

# add square

l=[1,2,3,4]
l2=[i**2 for i in l]

div=[i for i in range(1,41) if i%5==0]

languages=['python','js','c','c++']
language=[lang for lang in languages if lang.startswith('p') ]

# nested if

basket=['apple','guaba']
my_fruits=['apple','kiwi']

[fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]

[[i*h] for i in range(1,2) for h in range(1,2)]

l1=[1,2,3,4]
l2=[3,4,4,6]

[i*j for i in l1 for j in l2]

# reverse list
#itemwise

l=[1,2,3]
for i in l:
    print(i)
#  indexwise
for i in range(0,len(l)):
    print(l[i])


# zip

L1=[2,4,5,6]
L2=[4,5,6]
L3=list(zip(L1,L2))
[i+j for i,j in zip(L1,L2)]

# python all things are object

L=[1,2,print,type,input]
print(L)

# risky usage
a=[1,2,3,4]
b=a
print(a)
print(b)
a.append(4)
print(a)
print(b)