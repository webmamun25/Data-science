# email=input("Enter an email")
# password=input("Enter password")
#
# if email=='nitish@gmail.com' and password=="1234":
#     print("authenticate person")
# elif email=='nitish@gmail.com' and password!="1234":
#     print("incorrect password")
#     password=input('Enter password again')
#     if(password=='1234'):
#         print("welcome finally")
#     else:
#         print("Thumse na ho payega")
# else:
#     print("Not correct")


# min of 3 numbers
# a=int(input("first number"))
# b=int(input("sec number"))
# c=int(input("third number"))
# if a<b and a<c:
#     print("smallest is ",a)
# elif b<c:
#     print("smallest is ",b)
# else:
#     print("smallest is ",c)

# menu driven calculator

# fnum=int(input("enter the first number"))
# snum=int(input("enter the second number"))
#
# op=input("enter the operation")
#
# if op=='+':
#     print(fnum+snum)
# elif op=='-':
#     print(fnum-snum)
# elif op=='*':
#     print(fnum*snum)
# else:
#     print(fnum/snum)

# menu driven atm

menu=input("""
hi! how can i help you.
1.Enter 1 for pin change
2.Enter 2 for balance check
3.Enter 3 for withdrawl
4.Enter 4 for exit

""")

if menu=='1':
    print('pin change')
elif menu=='2':
    print('balance')
else:
    print('exit')