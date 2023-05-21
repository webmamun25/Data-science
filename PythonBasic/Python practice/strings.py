# find the length of a given string without using the len() function
s=input("enter the string:")
count=0
for i in s:
    count=count+1
print("length of string:",count)

# extract username from a given email

s=input('enter the email')

print(s.index('@'))

pos=s.index('@')
print(s[0:pos])
# count the frequency of a particular character in a provided string
s=input("enter the string:")
term=input("what would like to search for")
count=0
for i in s:
    if i==term:
        count+=1
print('frequencty',count)

# write a program which can remove particular string from a string
s=input("enter the string:")
term=input("what would like to remove")

result=[]
for i in s:
    if i!=term:
        result.append(i)
print(result)


# palindrom or not
#malyalam
s=input("enter the string:")
flag=True
for i in range(0,len(s)//2):
    if s[i] != s[len(s)-i-1]:
        flag=False
        print("Not a palindrome")
        break


if flag:
    print("pallindrome")

# count the number of words in a string without split

s=input("enter the string:")
temp=''
l=[]
for i in s:
    if i!=' ':
        temp=temp+i
    else:
        l.append(temp)
        temp=''

l.append(temp)
print(l)

# convert string to title case

s=input('enterthe string:')
L=[]
for i in s.split():
    L.append(i[0].upper()+i[1:].lower())
    print(' '.join(l))

# integer to  string

number=int(input("enter the number"))
digits='0123456789'
result=""
while number!=0:
    result=digits[number%10]+result
    number=number//10
print(result)



