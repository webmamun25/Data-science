# while loop
#
# number=int(input("enter the number:"))
# i=1
#
# while i<11:
#     print(number*i)
#     i+=1

# x=1
# while x<3:
#     print(x)
#     x+=1
# else:
#     print('Limit crossed')

# guessing game
# import random
# random_number=random.randint(1,100)
# guess=int(input("guess karo"))
# count=1
# while(random_number!=guess):
#
#     if(guess<random_number):
#         print("galat!guess higher")
#     else:
#         print("galat!guess lower")
#     guess = int(input("guess karo"))
#     count+=1
# else:
#     print("Correct guess")
#     print("attempts",count)


# for loop
for i in range(1,11):
    print(i)

curr_pop=10000
for i in range(10,0,-1):
    print(i,curr_pop)
    curr_pop=curr_pop-0.1*curr_pop

