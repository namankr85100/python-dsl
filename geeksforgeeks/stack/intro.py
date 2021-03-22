# Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).

# Mainly the following three basic operations are performed in the stack:

# Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
# Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
# Peek or Top: Returns top element of stack.
# isEmpty: Returns true if stack is empty, else false.


# import maxsize from sys module
#used to return infinite when stack is empty
from sys import maxsize

#function to create a stack .it initializez size of stack as 0
def createstack():
    stack=[]
    return stack

#stack is empty when stack size is 0
def isempty(stack):
    return len(stack)==0

#function to add an item to stack .it increses size by 1
def push(stack,item):
    stack.append(item)
    print(item+" pushed to stack")

#funstion to remove an item from stack.it decreases size by 1
def pop(stack):
    if(isempty(stack)):
        return str(-maxsize-1) #return minus infinite
    return stack.pop()

#function to return the top from stack without removing it
def peek(stack):
    if(isempty(stack)):
        return str(-maxsize-1) #return minus infinite
    return stack[len(stack)-1]

#driver program to test above functions
stack = createstack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))
print(pop(stack)+" popped from satck")
# Pros: Easy to implement. Memory is saved as pointers are not involved. 
# Cons: It is not dynamic. It doesn’t grow and shrink depending on needs at runtime.
 





print()
# implementaion of linked list
# Python program for linked list implementation of stack

# Class to represent a node


class StackNode:

	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:

	# Constructor to initialize the root of linked list
	def __init__(self):
		self.root = None

	def isEmpty(self):
		return True if self.root is None else False

	def push(self, data):
		newNode = StackNode(data)
		newNode.next = self.root
		self.root = newNode
		print ("pushed to stack" , data)

	def pop(self):
		if (self.isEmpty()):
			return float("-inf")
		temp = self.root
		self.root = self.root.next
		popped = temp.data
		return popped

	def peek(self):
		if self.isEmpty():
			return float("-inf")
		return self.root.data


# Driver code
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print ("popped from stack" ,stack.pop())
print ("Top element is" , stack.peek())
