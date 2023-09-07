#Binary Search using Iteration
def binary_search(ls,key):
    n=len(ls)
    left=0
    right=n-1
    mid=0
    while left <= right:
        mid=(left+right)//2
        if ls[mid]<key:
            left=mid+1
        elif ls[mid]>key:
            right=mid-1
        else:
            return mid
    return -1

if __name__=="__main__":
    ar=[2,4,6,10,12,14,16]
    key=14
    r=binary_search(ar,key)
    if r!=-1:
        print("%d present at %d position"%(key,(r+1)))
    else:
        print("%d doesnot exist in the list"%key)
        
