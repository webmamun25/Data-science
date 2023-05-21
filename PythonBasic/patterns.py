
# pattern-1
for i in range(5):
    for j in range(5):
        print('*',end=" ")

    print(' ')

# pattern-2

for i in range(5):
    for j in range(i):
        print('*',end=" ")

    print(' ')

# pattern-3
print()
for i in range(5):
    for j in range(5-i+1):
        print("*",end=" ")
    print(" ")


for i in range(5):
    for j in range(i):
        print('*',end=" ")

    print(' ')

for i in range(5):
    for j in range(4-i+1):
        print("*",end=" ")
    print(" ")
