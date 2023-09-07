#stack using linked list in python

class Node:
	def __init__(self,value):
		self.value = value 
		self.next = None
		
class Stack:
	def __init__(self):
		self.head = Node("head")
		self.size = 0
	def __stk__(self):
		temp = self.head.next
		out = ""
		while temp:
			out = out + str(temp.value) + "-->"
			temp = temp.next
		return out[:-2]
		
	def getSize(self):
		return self.size
	def isEmpty(self):
		return self.size ==0
		
	def push(self,value):
		node = Node(value)
		node.next = self.head.next
		self.head.next = node
		self.size +=1
		
	def pop(self):
		if self.isEmpty():
			raise Exception("the stack is empty")
		remove = self.head.next
		self.head.next = self.head.next.next
		self.size -=1
		return remove.value
		
	def peek(self):
		if self.isEmpty():
			raise Exception("The stack is empty")
		return self.head.next.value
		
		
if __name__=="__main__":
	stack=Stack()
	for i in range(1,11):
		stack.push(i)
	print(str(stack))
	for a in range(1,6):
		deleted = stack.pop()
		print("Popped element-->"+ str(deleted))
	for i in range:
		print(stack[i])










	