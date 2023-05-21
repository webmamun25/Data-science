# Dictionary in python is a collection of key and values

# characteristic

# 1.mutable 2.indexing has no meaning 3.keys can't duplicate 4.keys cant be mutable items

# creating dictionary
# empty dictionary
d={}
print(d)
# 1d dictionary
d1={"name":"jitish",'gender':'male'}
# mixed dict
d2={(1,2,3):1,'hello':'world'}
# 2d dict
student={
    'name':'nituish',
    'college':'bit',
    'subjects':{
        'dsa':50,
        'maths':67,
        'english':34
    }
}

# using sequence and dict function
d4=dict([('name','nitish'),(1,1),(2,2)])

# duplicate keys canot work
d5={'name':'nitish','name':'rahul'}
# mutable ites as keys not allowed
# d6={'name':'nitish',[1,2,3]:3}



# accessing item

# d1[0] not allowed

my_dict={'name':"nitish"}
my_dict['name']
my_dict.get('name')


# adding key value pair
my_dict['gender']='male'
print(my_dict)

# remove key_value pair

my_dict.pop('name')
my_dict.popitem()  #last item

del my_dict['name']
my_dict.clear()


# editing key value pair

my_dict['name']='mamun'

print(my_dict)


# dictionary operations

# membership operator works only keys not values .values for false keys for trues
'name' in my_dict

# loops

d={'name':'nitish','gender':'male'}
for i in d:
    print(i,d[i])


# len
len(d)
sorted(d)
min(d)
max(d)

# items/keys/values

print(d.items)
print(d.keys())
print(d.values())

# update
d1={1:2,2:4,4:8}
d2={4:7,6:8}
print(d1.update(d2))

# comprehension

# print 1st 10 numbers and their squares
{i:i**2 for i in range(1,11)}
# using existing dict

distances={'delhi':100,'mumbai':200}
{key:value*0.62 for (key,value) in distances.items()}

days=['sunday','monday','wednesday']
temp_c=[30.2,32.4,33,4]

{i:j for (i,j) in zip(days,temp_c)}

# using if condition

products={'phone':10,'laptop':0,'charger':32,'tablet':0}
{key:value for (key,value) in products.items( ) if value>0}

# nested comprehension

{i:{i:i*j for j in range(1,11)} for i in range(2,5)}