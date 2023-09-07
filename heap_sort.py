def heapify(ls,n,i):
    largest=i
    lc=2*i+1
    rc=2*i+2
    if lc<n and ls[i]<ls[lc]:
        largest=lc
    if rc<n and ls[largest]<ls[rc]:
        largest=rc
    if largest !=i:
        ls[i],ls[largest]=ls[largest],ls[i]
        heapify(ls,n,largest)

def heapsort(ls):
    n=len(ls)
    for i in range(n//2, -1, -1):
        heapify(ls,n,i)
    for i in range(n-1,0,-1):
        ls[i],ls[0]=ls[0],ls[i]
        heapify(ls,i,0)

if __name__=="__main__":
    ls=[12,21,13,31,14,41,15]
    n=len(ls)
    print("\nElements in the list are:",end=" ")
    for i in range(n):
        print(ls[i],end=" ")
    heapsort(ls)
    print("elements in the sorted array are:")
    for i in range(n):
        print(ls[i],end=" ")
