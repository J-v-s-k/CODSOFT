def add(m,n):
    display(m+n)
def subtract(m,n):
    display(m-n)
def multiply(m,n):
    display(m*n)
def divide(m,n):
    display(m/n)
def display(s):
    print(s)
try:
    while 1:
        print("----------------------------------")
        m=int(input("Enter First Number"))
        n=int(input("Enter Second Number"))
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\n")
        a=int(input("Enter Your Choice"))
        print("----------------------------------")
        if(a==1):
            add(m,n)
        elif(a==2):
            subtract(m,n)
        elif(a==3):
            multiply(m,n)
        elif(a==4):
            divide(m,n)
        elif(a==5):
            break
        else:
            print("Invalid Input.Please Try Again\n")
except ValueError:
    print("value error.Supports Only Integers")
except:
    print("Exception Raised.Please Try Again")