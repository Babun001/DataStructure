# # Let us say your expense for every month are listed below,
# # January - 2200
# # February - 2350
# # March - 2600
# # April - 2130
# # May - 2190

# # Create a dictionary to story my expenses for last 5 months
# dict1 = {
#     'January' : 2200,
#    'February' :2350,
#     'March' : 2600,
#     'April' : 2130,
#     'May' : 2190
# }

# # let's calculate how much i spent in last 5 months
# sum = 0 #sum variable that will stores the total value 
# for ele in dict1:
#     sum = sum +(dict1[ele]) # it will add the value one by one with the previous value of sum (Initially sum is 0)
# print("Total Expenses for 5 months ->", sum)

# '''1. In Feb, how many dollars you spent extra compare to January?'''

# ext = dict1['February'] - dict1['January']  # we can just subtrac value of feb to value of jan
# print(f"In February i spent {ext} extra compare to january")



# '''2. Find out your total expense in first quarter (first three months) of the year.'''

# exq = dict1['January']+dict1["February"]+dict1["March"] # we can add  value from a dictionary like that
# print("total expense in first quarter was ->", exq)



# '''3. Find out if you spent exactly 2000 dollars in any month'''

# #Let's create a function
# def searchInDict (item):    # item means any dictionary
#     for ele in item:        # to compare every value in dict1
#         if (item[ele]== 2000):
#             return ele      # Return element if the value is equal to 2000
#     return -1       # if not then return -1


# if(searchInDict(dict1) == -1):  # if the function returns -1 that means 2000 is not present in that dictionary and vise versa
#     print("No, I don't!")
# else:
#     print("Yes, I spent exactly 2000 dollars in ",searchInDict(dict1))



# '''4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list'''

# # dict1['June'] = 1980 
# # print(dict1)

# # another way

# dict1= {**dict1, **{'june': 1980}}
# print("After Adding june in array",dict1)


# '''5. You returned an item that you bought in a month of April and 
# got a refund of 200$. Make a correction to your monthly expense list based on this'''

# preAprilValue = dict1['April'] # We need the previous value of april to add the refunded money
# dict1['April'] = preAprilValue+200  # Add the refunded value with the previous value of april and update the dictionary

# print(dict1)


# '''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''

# # Next problems
# # You have a list of your favourite marvel super heros.

# heros=['spider man','thor','hulk','iron man','captain america']
# print("The initial array is ->",heros)

# '''1. Length of the list'''
# # Very simple
# print("Length of the array ->",len(heros))  # we can use len() function



# '''2. Add 'black panther' at the end of this list'''

# heros.append("black panther")   # append() method to add element in a array
# print("after adding black panther ->", heros)



# '''3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'''

# heros.pop()     # pop() is a in-build method or function to remove element from the tail of an array
# print("After dlt black panther ->", heros)
# heros.insert(3,'black panther')
# print("After adding black panther after hulk", heros)



# '''4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.'''

# # print(heros[1:3])
# heros[1:3] = ['doctor strange'] # here we use slice() function [start:end:step]
# print("After adding dr. strange->", heros)

# '''5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)'''
# heros.sort()
# print("The Sorted Array ->",heros)

'''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''

# Next problem

'''Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function'''

oddList = []
n = int(input("Enter Limit--->"))
for i in range(1,n):
    if (i%2!=0):
        oddList.append(i)

print(oddList)
