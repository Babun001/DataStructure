#Write a Program to insert a node 1. at the begining  2. at the end  3. insert at any specific position of a Single Linked List
class Node:
    def __init__(self, data):
        self.info=data
        self.link=None
class Single_LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beg(self, item):
        new_node=Node(item)
        if self.head is None:#checking linked list in empty or not
            self.head=new_node
            return
        else:
            new_node.link=self.head
            self.head=new_node
    def insert_at_end(self, item):
        new_node=Node(item)
        if self.head is None:#checking linked list in empty or not
            self.head=new_node
            return
        tmp=self.head
        while(tmp.link):
            tmp=tmp.link
        tmp.link=new_node
    def insert_at_pos(self, item, pos):
        new_node=Node(item)
        if(pos<1):
            print("\nInvalid Position")
        if(pos==1):
            new_node.link=self.head
            self.head=new_node
        else:
            tmp=self.head
            for i in range(1, pos-1):
                tmp=tmp.link
            if(tmp!=None):
                new_node.link=tmp.link
                tmp.link=new_node
    def display(self):
        tmp=self.head
        while tmp is not None:
            print(tmp.info,end=" ")
            tmp=tmp.link

if __name__=="__main__":
    sl=Single_LinkedList()
    sl.insert_at_beg(10)
    sl.insert_at_beg(20)
    sl.display()
    sl.insert_at_end(30)
    sl.insert_at_end(40)
    print("\n")
    sl.display()
    sl.insert_at_pos(50,4)
    print("\n")
    sl.display()
    
                
            
