# A set is an unrodered collection of items

# every set element is unique and must be immutable

# characteristics
#     1.unordered
#     2.Mutable
#     3.No duplicates
#     4.Can't contain mutable data types

# creating sets
# empty set
s=set()
print(s)

s1={1,2,3}
print(s1)

s2={1,2,3,{1,2,3}} # error mutable within mutable is not possible

s3={1,'hello',4.5,True} #Trueis not print bcs true denote 1 in python
# type conversion

s4=set([1,2,3])
print(s4)

s5={1,2,23,111,1,1,1}
print(s5)

s1={1,2,3}
s2={3,2,1}
print(s1==s2)
# order doesn't matter

# accessing item

s1={1,2,3,4}
s1[0] # changes not allow indexing or slicing

# editing item
# editing are not allowed

# adding item
s={1,2,3,4}
s.add(5)
print(s)
# multiple item
s.update([5,5,6,7])
print(s)

# deleting items
s={1,2,2,2}
print(s)
del(s)
print(s)
s.discard(2)
print(s)

s.remove(2)
print(s)

# discard doesnot show error when this value is not in set but remove show error
# random deletion
s.pop()
print(s)
# empty set
s.clear()
print(s)

# sets operation

s1={1,2,4}
s2={4,5,6}
# union
print(s1|s2)

# intersection
print(s1&s2)
# difference
print(s1-s2)

# symmetric difference
print(s1^s2)
# membership test
1 not in s1
# iteration
for i in s1:
    print(i)


# function
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s))

# union/update

s1.union(s2)
s1.update(s2)

# intersection/intersection_update

s1.intersection(s2)
s1.intersection_update(s2)

# difference
s1.difference(s2)
s1.difference_update(s2)

# symmetric
s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)

# isdisjoint-->there is any common element both set?

s1={1,2,3,4}
s2={3,4,5,6}
s1.isdisjoint(s2)
# issubset
s1={1,2,3,4,5}
s2={2,3,4,5}
s2.issubset(s1)

# superset
s1.issubset(s2)

# copy

s1={1,2,3}
s2=s1.copy()
print(s1)
print(s2)

# frozenset  # immutable version

fs1=frozenset([1,2,3])

fs2=frozenset([2,3,4])
print(fs1 | fs2)

# add delete not work update discard not work

# read only application used for

# 2d sets

fs=frozenset([1,2,frozenset([3,4])])
print(fs)

# comprehension

print({i for i in range (2,22) if i>5})


