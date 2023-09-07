#Insertion sort in Python

'''a = [10,8,9,45,69,74]
print("The initial Array--->", a)

for i in range(0,len(a)):
	for j in range(i+1,len(a)-1):
		while(a[j]<a[i]):
			temp = a[i]
			a[i] = a[j]
			a[j] = temp
			

print("Afterr Insertion sort--->",a)'''


#Selection Sort in python

'''a = [10,8,9,45,69,74]
print("The initial Array--->", a)

for i in range(0,len(a)):
	for j in range(i+1, len(a)):
		while(a[i]>a[j]):
			temp = a[i]
			a[i] = a[j]
			a[j] = temp
			
		
print("after sorting --- >", a)'''



# Bubble sort in python

a = [10,8,9,45,69,74]
print("The initial array", a)
for i in range(0, len(a)):
	for j in range(0, len(a)-1-i):
		if (a[j]>a[j+1]):
			temp = a[j]
			a[j] = a[j+1]
			a[j+1] = temp
			
print("After Bubble sort", a)























