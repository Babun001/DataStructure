#Binary Search using Recursion:
def binary_search_rec(ls,left,right,key):
    mid=0
    if left > right:
        return -1
    else:
        mid=(left+right)//2
        if ls[mid]==key:
            return mid
        elif ls[mid] > key:
            return binary_search_rec(ls,left,mid-1,key)
        else:
            return binary_search_rec(ls,mid+1,right,key)
        

if __name__=="__main__":
    ar=[2,4,6,10,12,14,16]
    left=0
    right=len(ar)-1
    key=int(input("Enter Element to be searched:"))
    r=binary_search_rec(ar,left,right,key)
    if r!=-1:
        print("%d present at %d position"%(key,(r+1)))
    else:
        print("%d doesnot exist in the list"%key)
        
