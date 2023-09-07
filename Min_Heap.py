import heapq
class MinHeap:
    def __init__ (self, heap):
        heapq.heapify(heap)
        self.heap=heap

    def insert(self, item):
        heapq.heappush(self.heap, item)

    def delete_heap(self):
        heapq.heappop(self.heap)

    def root_element(self):
        return self.heap[0]

    def display(self):
        print(self.heap)


if __name__=="__main__":
    ls=[45, 36, 54, 27, 63, 72, 61, 18]
    hp=MinHeap(ls)
    print("Min Heap elements are:")
    hp.display()
    hp.insert(42)
    print("Min heap elements after insertion are:")
    hp.display()
    x=hp.root_element()
    hp.delete_heap()
    print("Delete element from the Min Heap is:",x)
    print("Min heap elements after deletion are:")
    hp.display()
