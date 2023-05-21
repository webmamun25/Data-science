# conventional way
a=10
b=50
temp=a
a=b
b=temp
print(a,b)

# python way

a=10
b=50

a,b=b,a
print(a,b)