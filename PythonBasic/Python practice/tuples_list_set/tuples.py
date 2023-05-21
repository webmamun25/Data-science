# tuple is similar to list.but tuple is immutable but list is mutable
# characteristics--->1.ordered 2.unchangeable 3.Allows duplicate

t1=()
print(t1)

# creat a tuple using single item

t2=(2,)
type(t2)
# homogenous
t3=(1,2,3,4)
# hetrogenous
t4=(1,2,'hello',[12,12])
# nested tuple
t5=(12,12,344,(4,5))
# type conversion
t6=tuple('jel')

# accessing item

print(t3[0])
print(t3[-1])

# slicing
print(t3[0:4:2])
print(t3[::-1])
print(t5[-1][0])

# editing item
# cannot edit because editable

# adding item
# not possible

# deleting items
# del for full tuple delete but not portion deletion
#
# del(t3)
# del(t3[1])  #not possible


# operation in tuple

t1=(1,2,3,4)
t2=(5,5,6,76,8)
print(t1+t2)
print(t1*3)
print(1 in t1)

for i in t1:
    print(i)

# tuple functions

t=(1,2,4,5)
sum(t)
min(t)
max(t)
sorted(t,reverse=True)

print(t.count(5))

print((t.index(5)))

# difference between list and tuples

    # 1.Syntax-->(),[]
    # 2.Mutabiltiy-->tuple immutable
    # 3.Speed-->tuple is faster immutable is faster than mutable
    # 4.Memory-->tuple less memory
    # 5.Built in functionality-->list has more
    # 6.Error prone-->list is more error prone tuple is easy to debug
    # 7.Usability-->just read only not change use tuple

# special syntax

a,b,c=(1,2,3)

a,b=(1,2,3)
a=1
b=2
a,b=b,a
a,b,*others=(1,2,3,4)
print(a,b)
print(others)

# zipping tuple
a=(1,2,3,4)
b=(5,6,7,8)
tuple(zip(a,b))