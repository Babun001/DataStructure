# Creation of Double Linked List in Python:
class Node:
    def __init__(self, data):
        self.info=data
        self.previous=None
        self.next=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self, item):
        new_node=Node(item)
        if(self.head==None):#linked list is initialy empty
            self.head=self.tail=new_node
            new_node.previous=None
            new_node.next=None
        else:
            self.tail.next=new_node
            new_node.previous=self.tail
            new_node.next=None
            self.tail=new_node
    def insert_at_beg(self, item):
        new_node=Node(item)
        if(self.head==None):
            self.head=self.tail=new_node
            new_node.previous=None
            new_node.next=None
        else:
            new_node.next=self.head
            self.head.previous=new_node
            self.head=new_node
            new_node.previous=None
    def display(self):
        tmp=self.head
        if(self.head==None):
            print("\nNothing to display!")
            return
        print("\nElements in the Double Linked List are:")
        while(tmp!=None):
            print(tmp.info,end=" ")
            tmp=tmp.next

if __name__=="__main__":
    dl=DoubleLinkedList()
    def switch(y):
        switcher={
            1:dl.create(20),
            2:dl.display(),
            3:dl.insert_at_beg(10),
        }
        return switcher.get(y,"Nothing to Do!")
    print("\nPress 1 to create 2 to display 3 to insert at begining")
    s=int(input("Enter your choice:"))
    switch(s)
    '''dl.display()
    n=int(input("\nHow many nodes you want to create:"))
    for i in range(n):
        x=int(input("\nEnter the value for node%d:"%(i+1)))
        dl.create(x)
    dl.display()
    dl.insert_at_beg(10)
    dl.display()'''
            
        
