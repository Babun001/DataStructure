def mergesort(ls):
    if(len(ls)>1):
        mid=len(ls)//2
        left=ls[:mid]
        right=ls[mid:]
        mergesort(left)
        mergesort(right)
        i,j=0,0
        k=0
        while((i<len(left))and(j<len(right))):
            if(left[i]<=right[j]):
                ls[k]=left[i]
                i+=1
            else:
                ls[k]=right[j]
                j+=1
            k+=1
        while(i<len(left)):
            ls[k]=left[i]
            i+=1
            k+=1
        while(j<len(right)):
            ls[k]=right[j]
            j+=1
            k+=1

if __name__=="__main__":
    ls=[12,21,13,31,14,41,15]
    n=len(ls)
    print("\nElements in the list are:",end=" ")
    for i in range(n):
        print(ls[i],end=" ")
    mergesort(ls)
    print("\nElements of the list in sorted order are:",end=" ")
    for i in range(n):
        print(ls[i],end=" ")            
