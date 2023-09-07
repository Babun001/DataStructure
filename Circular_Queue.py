class Circular_Queue:
    def __init__(self, MAX): # initializing the class
        self.size=MAX
        self.queue=[None]*MAX # [None for i in range(MAX)]
        self.front=self.rear=-1
        
    def enqueue(self, item):
        if (self.front==(self.rear+1)% self.size): # Condition for the Circular Queue is Full
            print("\nInsertion not possible as the Queue is full")
        elif (self.front==-1): # Checking for the Circular Queue is initialy empty or not
            self.front=0
            self.rear=0
            self.queue[self.rear]= item
        else: # Some elements are already there in the Circular Queue
            self.rear=(self.rear+1)%self.size # Condition for increasing the rear value to insert some element in the Circular Queue
            self.queue[self.rear]=item
    
    def dequeue(self):
        if (self.front==-1): # Checking for the Circular Queue is initialy empty or not
            print("\nNothing to delete as the Queue is empty")
        elif (self.front==self.rear): # Checking there is only one element in the Circular Queue or not
            x=self.queue[self.front]
            self.front=self.rear=-1
            return x
        else: # More than one element is present in the Circular Queue
            x=self.queue[self.front]
            self.front=(self.front+1) % self.size # Condition for increasing the front value to delete some element from the Circular Queue
            return x
        
    def display(self):
        if (self.front==-1): # Checking for the Circular Queue is initialy empty or not
            print("\nNothing to display as the Queue is empty")
        elif (self.rear >= self.front):
            print("\nElements in the Circular Queue are:")
            for i in range(self.front,self.rear+1):
                print(self.queue[i], end=" ")
        else:
            print("\nElements in the Circular Queue are:")
            for i in range(self.front,self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear+1):
                print(self.queue[i], end=" ")
                
if __name__=="__main__":
    cq=Circular_Queue(6)
    cq.display()
    cq.enqueue(2)
    cq.enqueue(4)
    cq.enqueue(6)
    cq.enqueue(4.5)
    cq.display()
    print("\nFirst Deleted value=", cq.dequeue())
    print("\nSecond Deleted value=", cq.dequeue())
    cq.display()
    cq.enqueue(12)
    cq.enqueue(3.9)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.display()
    cq.enqueue(8)


#Assignment: Develop Stack and Linear Queue in the above way. Without using append(), insert(), pop().
