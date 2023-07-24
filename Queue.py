queue=[]
def Enqueue():
    print("Enter the elment to Enqueue: ")
    queue.append(input())
def Display():
    print(queue)
def Dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e=queue.pop(0)
        print("removed Element",e)
def IsEmpty():
    if not queue:
        print("Queue is empty")
    else:
        print("Queue is not empty")
msg="""
    Select the operation to perform Queue operations 
    1.Enqueue 
    2.Dequeue 
    3.Display 
    4.Empty
    """
while True:
    print(msg)
    choice=int(input())
    if choice==1:
        Enqueue()
    elif choice==2:
        Dequeue()
    elif choice==3:
        Display()
    elif choice==4:
        IsEmpty()