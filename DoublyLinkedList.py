class Node:
    def __init__(self,data) -> None:
        self.pref=None
        self.data=data
        self.nref=None
class DoublyLL:
    def __init__(self) -> None:
        self.head=None

    def display(self):
        if self.head is None:
            print("Linked List is Empty")    
        else:
            temp=self.head
            while(temp is not None): 
                print(temp.data)
                temp=temp.nref

    def reverse(self):
        if self.head is None:
            print("Linked List is Empty")    
        else:
            temp=self.head
            while(temp.nref is not None):
                temp=temp.nref
            while(temp.pref is not None):
                print(temp.data)
                temp=temp.pref
            if(temp.nref):
                print(temp.data)
        # print("hu",temp.data,temp.pref)

    def insert_empty(self,data):
        n1=Node(data)
        if self.head is None:
            self.head=n1
    def insert_begining(self,data):
        n1=Node(data)
        n1.nref=self.head
        self.head.pref=n1
        self.head=n1
    def insert_ending(self,data):
        n1=Node(data)
        temp=self.head
        while(temp.nref is not None):
            temp=temp.nref
        temp.nref=n1    
        n1.pref=temp
    def insert_after(self,data,x):
        n1=Node(data)
        temp=self.head
        while(temp is not None):
            # print(temp,x)
            if temp.data==x:
                n1.nref=temp.nref
                n1.pref=temp
                temp.nref=n1
                temp.nref.pref=n1
                break
            temp=temp.nref
    def insert_before(self,data,x):
        n1=Node(data)
        temp=self.head
        if temp.data==x:
            n1.nref=temp
            temp.pref=n1
            self.head=n1
        else:
            while(temp is not None):
                if temp.nref.data==x:
                    n1.nref=temp.nref
                    n1.pref=temp
                    temp.nref=n1
                    temp.nref.pref=n1
                    break
                temp=temp.nref
        
    def del_begining(self):
        self.head=self.head.nref
        self.head.pref=None
    def del_end(self):
        temp=self.head
        while temp.nref is not None:
            temp=temp.nref
        temp.pref.nref=None
    def delete(self,x):
        if self.head.data==x:   
            self.del_begining()
        else:
            temp=self.head
            while(temp.nref is not None):
                if(temp.data==x):
                    temp.nref.pref=temp.pref
                    temp.pref.nref=temp.nref
                    break
                temp=temp.nref
            self.del_end()


        
dl=DoublyLL()
dl.insert_empty(1)
dl.insert_before(0,1)
dl.insert_begining(11)
dl.insert_ending(10)
dl.insert_after(2,1)
dl.delete(10)
dl.display()