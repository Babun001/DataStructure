import heapq
class MaxHeap:
    def __init__ (self, heap):
        heapq.heapify(heap)
        self.heap=heap

    def insert(self, item):
        heapq.heappush(self.heap, -1*item)

    def delete_heap(self):
        heapq.heappop(self.heap)

    def root_element(self):
        return self.heap[0]

    def display(self):
        for i in self.heap:
            print(-1*i, end=" ")
        print("\n")


if __name__=="__main__":
    ls=[45, 36, 54, 27, 63, 72, 61, 18]
    l=[]
    for i in range(len(ls)):
        y=ls[i]
        l.append(-1*y)
    hp=MaxHeap(l)
    print("Max Heap elements are:")
    hp.display()
    hp.insert(42)
    print("Max heap elements after insertion are:")
    hp.display()
    x=hp.root_element()
    hp.delete_heap()
    print("Delete element from the Max Heap is:",-1*x)
    print("Max heap elements after deletion are:")
    hp.display()
