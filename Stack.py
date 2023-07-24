stack=[]
def push():
    print("Enter the elment to push: ")
    stack.append(input())
    print(stack)
def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("the peek element is ",stack[-1])    

def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("removed Element",e)
        print(stack)
def IsEmpty():
    if not stack:
        print("stack is empty")
    else:
        print("Stack is not empty")
while True:
    print("Select the operation to perform stack operations 1 .push 2.pop 3.peek 4.empty")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        peek()
    elif choice==4:
        IsEmpty()

