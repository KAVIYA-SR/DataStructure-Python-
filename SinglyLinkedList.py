class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked List is Empty")    
        else:
            temp=self.head
            while(temp is not None):
                print(temp.data,end=" ")
                temp=temp.next
    def add_begin(self,data):
        n1=Node(data)
        n1.next=self.head
        self.head=n1
    def add_end(self,data):
        n1=Node(data)
        if self.head is None:
            self.head=n1
        else:
            temp=self.head
            while (temp.next is not None):
                temp=temp.next    
            temp.next=n1
    def add_after(self,data,prev_data):
        n1=Node(data)
        temp=self.head
        while(temp.next is not None):
            if temp.data==prev_data:
                n1.next=temp.next
                temp.next=n1
                break
            temp=temp.next
    def remove(self):
        temp=self.head
        if temp is None:
            print("Linked List is Empty")
        else:
            self.head=self.head.next

    def remove_end(self):
        temp=self.head
        if temp is None:
            print("Linked List is Empty")
        else:
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None    
    def delete(self,data):
        temp=self.head
        if temp is None:
            print("Linked List is Empty")
        else:
            if temp.data==data:
                self.head=self.head.next
            else:
                while temp.next is not None:
                    if temp.next.data==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    
l1=LinkedList()
l1.add_begin(8)          
l1.add_begin(5)           
l1.add_begin(13)        
l1.add_begin(1)
l1.add_end(90)   
# l1.remove()   
# l1.remove_end()
l1.delete(90)
l1.display()     

node1=Node(1)        