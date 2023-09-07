def selectionsort(ls):
    n=len(ls)
    for i in range(n):
        min=ls[i]
        loc=i
        for j in range(i+1,n):
            if(ls[j]<min):
                min=ls[j]
                loc=j
        if(loc!=i):
            tmp=ls[i]
            ls[i]=ls[loc]
            ls[loc]=tmp
if __name__=="__main__":
    ls=[12,21,13,31,14,41,15]
    n=len(ls)
    print("\nElements in the list are:",end=" ")
    for i in range(n):
        print(ls[i],end=" ")
    selectionsort(ls)
    print("\nElements of the list in sorted order are:",end=" ")
    for i in range(n):
        print(ls[i],end=" ")
        
