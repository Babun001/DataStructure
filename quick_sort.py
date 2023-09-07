def split_list(ls,beg,end):
    left=beg
    right=end
    loc=beg
    flag=0
    while(flag!=1):
        while((ls[loc]<=ls[right])and(loc!=right)):
            right-=1
        if(loc==right):
            flag=1
        elif (ls[loc]>ls[right]):
            tmp=ls[loc]
            ls[loc]=ls[right]
            ls[right]=tmp
            loc=right
        if(flag!=1):
            while((ls[loc]>=ls[left])and(loc!=left)):
                left+=1
            if(loc==left):
                flag=1
            elif(ls[loc]<ls[left]):
                tmp=ls[loc]
                ls[loc]=ls[left]
                ls[left]=tmp
                loc=left
    return loc

def quicksort(ls,left,right):
    if left<right:
        loc=split_list(ls,left, right)
        quicksort(ls,left,loc-1)
        quicksort(ls,loc+1,right)

if __name__=="__main__":
    ls=[12,21,13,31,14,41,15]
    n=len(ls)
    print("\nElements in the list are:",end=" ")
    for i in range(n):
        print(ls[i],end=" ")
    quicksort(ls,0,n-1)
    print("\nElements of the list in sorted order are:",end=" ")
    for i in range(n):
        print(ls[i],end=" ")
