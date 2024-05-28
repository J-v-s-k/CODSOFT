#to do list
def addTask(task):
    task.append(input('enter your Task To Do'))
    print("task added successfully")
    return task
def delTask(task):
    display(task)
    r=int(input("enter a task number to delete"))
    if(r>0 and r<=len(task)):
        task.pop(r-1)
        print("Successfully Deleted")
    else:
        print("Invalid Input")
    return task;
def display(task):
    print("Remaining Tasks To Complete")
    print("-------------------------------------------")
    if(len(task)==0):
            print("No Tasks Are Left")
    else:
        for i in range(len(task)):
                print(i+1,task[i])
    print("-------------------------------------------")
task=[]
while 1:
    print("-------------------------------------------")
    print("1.Add a Task\n2.Remove a Task\n3.View Tasks\n4.Exit\n")
    print("-------------------------------------------")
    try:
        n=int(input("Enter Your Choice\n"))
        if(n==1):
            task=addTask(task)
        elif(n==2):
            task=delTask(task)
        elif(n==3):
            display(task)
        elif(n==4):
            break
        else:
            print("Invalid Input.Please Try Again")
    except ValueError:
        print("Only Integers Are Supported")
    except:
        print("SomeThing Went Wrong")
    
        

