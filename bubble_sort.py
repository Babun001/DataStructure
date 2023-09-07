#Bubble Sort in Python:
def bubble_sort(ls):
    n=len(ls)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if ls[j]>ls[j+1]:
                tmp=ls[j+1]
                ls[j+1]=ls[j]
                ls[j]=tmp
    return ls
if __name__ =="__main__":
    l=[12,21,13,31,14,41]
    r=[]
    r=bubble_sort(l)
    print("Sorted Array is:",r)
    
        
