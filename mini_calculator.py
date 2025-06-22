
    #welcome to my mini computer
#take user input
print("|=====================|")
print("|   MINI CALCULATOR   |")
print("|=====================|\n")
while True:
    n1 =int(input("enter first number : "))
    #sign=input("enter the sign(+,-,*,/): ")
    n2 =int(input("enter second number : "))
    sign=input("enter the sign(+,-,*,/): ")

    if sign=='+':
        print("result is",(n1+n2))
        

    elif sign=='-':
        print("result is",(n1-n2))

    elif sign=='*':
        print("result is",(n1*n2))

    elif sign=='/':
        if(n2==0):
            print("error division by zero")
        else:
        
   
            print("result is",(n1/n2))
    else:
        print("choose the currect sign")
    print(" ")
    again=input("do you want to use again it (y/n): ")
    if again.lower()!='y':
        print("thank you for using calculator 😇 & Good bye 🙋‍♂️")
        break
            
    
        