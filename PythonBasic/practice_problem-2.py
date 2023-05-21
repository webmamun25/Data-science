# program-Find the sum of a 3 digit number entered by the user

num=int(input("Enter a 3 digit number:"))
a=num%10
num=num//10
b=num%10
num=num//10
c=num%10

print(a+b+c)

# population each year increase 10% .population at the end of each of the last 10 years

curr_prop=10000
for i in range(10,0,-1):
    print(i,round(curr_prop))
    curr_prop=curr_prop/1.1


# sequence sum--> 1/1!+2/2!+3/3!+....
import math

n=int(input('Enter n:'))
result=0
fact=1
for i in range(1,n+1):

    result=result+i/math.factorial(i)
print(result)
