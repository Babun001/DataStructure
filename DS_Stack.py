# Write a Program to implement the concept of Stack:
class Stack:
    def __init__(self, MAX): # initializing the class using constructor
        self.size=MAX
        self.arr=[None]*MAX # [None for i in range(MAX)]
        self.top=-1
    def push(self, item):
        if (self.top== self.size-1):
            print("\nStack is Full!")
        else:
            self.top=self.top+1
            self.arr[self.top]=item
    def pop(self):
        if (self.top==-1):
            print("\nStack is Empty!")
        else:
            x=self.arr[self.top]
            self.top=self.top-1
            return x
    def display(self):
        if (self.top==-1):
            print("\nNothing to display!")
        else:
            print("\nElements in the Stack are:")
            for i in range(0,self.top+1):
                print(self.arr[i], end=" ")

if __name__=="__main__":
    st=Stack(7)
    st.display()
    st.push(2)
    st.push(4)
    st.push(6)
    st.display()
    print("\nFirst deleted element is:",st.pop())
    print("\nSecond deleted element is:",st.pop())
    st.push(8)
    st.push(10)
    st.display()
        
