def insertionsort(ls):
    for i in range(1,n):
        tmp=ls[i]
        j=i-1
        while((tmp<ls[j])and(j>=0)):
            ls[j+1]=ls[j]
            j-=1
        ls[j+1]=tmp
if __name__=="__main__":
    ls=[12,21,13,31,14,41,15]
    n=len(ls)
    print("\nElements in the list are:",end=" ")
    for i in range(n):
        print(ls[i],end=" ")
    insertionsort(ls)
    print("\nElements of the list in sorted order are:",end=" ")
    for i in range(n):
        print(ls[i],end=" ")
