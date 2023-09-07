# Implementation of Double Linked List in Python:
class Node:
    def __init__(self, data):
        self.info=data
        self.previous=None
        self.next=None
class Double_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self, item):
        new_node=Node(item)
        if(self.head==None):#checking the linked list is initially empty or not
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.previous=self.tail
            self.tail=new_node

    def insert_at_beg(self, item):
        new_node=Node(item)
        if(self.head==None):
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.previous=new_node
            self.head=new_node

    def insert_at_end(self, item):
        new_node=Node(item)
        if(self.head==None):
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.previous=self.tail
            self.tail=new_node

    def insert_at_pos(self, item, pos):
        new_node=Node(item)
        if(pos<1):
            print("\nInvalid Position!")
            return
        if(pos==1):
            new_node.next=self.head
            self.head.previous=new_node
            self.head=new_node
        else:
            tmp=self.head
            for i in range(1, pos-1):
                tmp=tmp.next
            if(tmp!=None):
                new_node.previous=tmp
                new_node.next=tmp.next
                tmp.next.previous=new_node
                tmp.next=new_node

    def delete_from_beg(self):
        if self.head is None:
            print("\nNothing to delete!")
            return
        tmp=self.head
        x=tmp.info
        self.head=self.head.next
        tmp.next.previous=None
        tmp=None
        return x

    def delete_from_end(self):
        if self.head is None:
            print("\nNothing to delete!")
            return
        tmp=self.tail
        x=tmp.info
        self.tail=self.tail.previous
        tmp.previous.next=None
        tmp=None
        return x

    def delete_from_pos(self, pos):
        if self.head is None:
            print("\nNothing to delete!")
            return
        if(pos<1):
            print("\nInvalid Position!")
            return
        if(pos==1):
            tmp=self.head
            x=tmp.info
            self.head=self.head.next
            tmp.next.previous=None
            tmp=None
            return x   
        else:
            tmp=self.head
            for i in range(1, pos):
                tmp=tmp.next
            if(tmp!=None):
                x=tmp.info
                tmp.next.previous=tmp.previous
                tmp.previous.next=tmp.next
                tmp=None
                return x
            
    def display(self):
        tmp=self.head
        if(self.head==None):
            print("\nNothing to display!")
            return
        print("\nElements in the Double Linked list are:")
        while(tmp!=None):
            print(tmp.info,end=" ")
            tmp=tmp.next

if __name__=="__main__":
    dl=Double_linked_list()
    n=int(input("\nEnter how many nodes you want to create:"))
    for i in range(n):
        x=int(input("\nEnter the value for node%d :"%(i+1)))
        dl.create(x)
    dl.display()
    dl.insert_at_beg(25)
    dl.display()
    dl.insert_at_end(40)
    dl.display()
    dl.insert_at_pos(100,4)
    dl.display()
    r1=dl.delete_from_beg()
    print("\nDeleted element from the Begining is:",r1)
    dl.display()
    r2=dl.delete_from_end()
    print("\nDeleted element from the End is:",r2)
    dl.display()
    r3=dl.delete_from_pos(4)
    print("\nDeleted element from the Position is:",r3)
    dl.display()
