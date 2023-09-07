class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enQueue(self,element):
        self.items.insert(0,element)
        # self.items.append(element)
    def deQueue(self):
        if self.isEmpty():
            raise Empty("Queue is Empty, nothing to delete")
        return self.items.pop()
        # return self.items.pop(0)
    def size(self):
        return len(self.items)

# Assignment: Complete the above program.
