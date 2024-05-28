import random
def compchoice():
    cc=['Rock','Paper','Scissors']
    computer=random.choice(cc)
    return computer
def winorlose(n,won,tie,lose):
    p=compchoice()
    if((n==1 and p=='Rock') or (n==2 and p=='Paper') or (n==3 and p=='Scissors')):
        return (p,'tie',won,(tie+1),lose)
    elif((n==1 and p=='Scissors') or (n==2 and p=='Rock') or (n==3 and p=='Paper')):
        return (p,'You Won',(won+1),tie,lose)
    elif((n==1 and p=='Paper') or (n==2 and p=='Scissors') or(n==3 and p=='Rock')):
        return (p,'You Lose',won,tie,(lose+1))
def reset():
    return(won:=0,tie:=0,lose:=0)
def userchoice(n):
    if(n==1):
        return 'Rock'
    elif(n==2):
        return 'Paper'
    elif(n==3):
        return 'Scissors'
won=tie=lose=0
while 1:
    print('---------------------------------')
    print("1.Rock\n2.Paper\n3.Scissors\n4.PlayAgain\n5.Exit\n")
    print('---------------------------------')
    n=int(input("Enter Your Choice\n"))
    if(n==1 or n==2 or n==3):
        c,k,won,tie,lose=winorlose(n,won,tie,lose)
        print('Your Choice=',userchoice(n))
        print('Computer Choice=',c)
        print(k)
        print('Wins=',won)
        print('Ties=',tie)
        print('Loses=',lose)
    elif(n==4):
        won,tie,lose=reset()
    elif(n==5):
        break
    else:
        print("Invalid Input.Please Try Again")