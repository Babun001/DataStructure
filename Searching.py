#Linear Search and Binary Search in python
'''def linear(arr,item):
    for i in range(0,len(arr)):
        if (arr[i]==item):
            return i
    return 0

arr = [7,6,45,8,1,0,9]
item = (int(input("Enter Search element")))
result = linear(arr,item)

if (result == 0):
    print("{} Element is not present in this array".format(item))
print("{} is present in this array at {} index".format(item,result))'''


#Binary Search in python

def Bsearch(arr,item,high,low):
    if high>=low:
        mid = (high+low)//2

        if (arr[mid]==item):
            return mid
        elif(arr[mid]>item):
            return Bsearch(arr,item,mid+1,high)
        else:
            return Bsearch(arr,item,low,mid-1)
    else:
        return -1

arr = [4,8,9,12,15,150]
item = int(input("Enter Element to Search--->"))
high=len(arr)
low = 0
result = Bsearch(arr,item,high,low)
if (result ==  -1):
    print("{} is not present in this array".format(item))
print("{} is present in this array at {} index".format(item,result))
#D:\DataSructure code pdf\Searching.py