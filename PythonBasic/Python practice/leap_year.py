user_guess=int(input("Enter a number"))

if(user_guess%400==0):
    print("this is leaf year")
elif(user_guess%4==0 and user_guess%100!=0):
    print("This is leaf year")
else:
    print("this is not leaf year")