#Implementing Stack using Python:
class Node:
    def __init__(self, data):
        self.info=data
        self.link=None
class Linked_Stack:
    def __init__(self):
        self.top=None
        self.last=None
    def isEmpty(self):
        if(self.top==None):
            return True
        else:
            return False
    def push(self, item):
        new_node=Node(item)
        if self.top==None:
            self.top=self.last=new_node
        else:
            self.last.link=new_node
            self.last=self.last.link
    def pop(self):
        if self.isEmpty():
            print("\nNothing to Delete from the Stack!")
            return
        else:
            tmp=self.top
            ptr=self.top
            while(tmp.link):
                ptr=tmp
                tmp=tmp.link
            ptr.link=None
            print("\nDeleted Element=",tmp.info)
    def display(self):
        tmp=self.top
        if self.isEmpty():
            print("\nNothing to Display!")
        else:
            print("\nElements in the Stack are:")
            while(tmp!=None):
                print(tmp.info,end=" ")
                tmp=tmp.link

if __name__=="__main__":
    st=Linked_Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    st.push(40)
    st.display()
    st.pop()
    st.display()
    st.pop()
    st.display()
    
            
