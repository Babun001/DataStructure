# Write Python functions to 1. Create 2. Delete from Begining  3. Delete from end and 4. Display in a Single Linked List:
class Node:
    def __init__(self, data):
        self.info=data
        self.link=None
class Single_LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None
    def create(self, item):
        if self.head is None:
            self.head=Node(item)
            self.last_node=self.head
        else:
            self.last_node.link=Node(item)
            self.last_node=self.last_node.link
            
    def delete_from_beg(self):
        if self.head is None:
            print("\nNothing to Delete!")
            return
        tmp=self.head
        x=tmp.info
        self.head=self.head.link
        tmp=None
        return x

    def delete_from_end(self):
        if self.head is None:
            print("\nNothing to delete!")
            return
        last=self.head
        tmp=self.head
        while(last.link):  
            tmp=last
            last=last.link
        x=last.info
        last=None
        tmp.link=None
        return x

    def delete_from_pos(self,pos):
        if(pos<1):
            print("\nEnter a valid position to delete!")
            return
        if (pos==1): # Delete from begining
            tmp=self.head
            x=tmp.info
            self.head=self.head.link
            tmp=None
            return x
        else:
            tmp=self.head
            prev=self.head
            for i in range(1,pos):
                prev=tmp
                tmp=tmp.link
            x=tmp.info
            prev.link=tmp.link
            tmp=None
            return x
            
    def display(self):
        tmp=self.head
        while tmp is not None:
            print(tmp.info,end=" ")
            tmp=tmp.link

if __name__=="__main__":
    sl=Single_LinkedList()
    n=int(input("How many nodes you want to create:"))
    for i in range(n):
        x=int(input("\nEnter the value of node %d: "%(i+1)))
        sl.create(x)
    print("\nElements in the Single Linked List are:",end=" ")
    sl.display()
    r1=sl.delete_from_beg()
    print("\nDeleted element from Begining is:",r1)
    sl.display()
    r2=sl.delete_from_end()
    print("\nDeleted Element from End is:",r2)
    sl.display()
    p=int(input("\nEnter the position from where you want to delete:"))
    r3=sl.delete_from_pos(p)
    print("\nDeleted elemnet from the position %d is %d"%(p,r3))
    sl.display()
