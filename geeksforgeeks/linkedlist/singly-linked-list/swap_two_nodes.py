# Given a linked list and two keys in it, swap nodes for two given keys. Nodes should be swapped by changing links. Swapping data of nodes may be expensive in many situations when data contains many fields. 
# It may be assumed that all keys in the linked list are distinct.
# Examples: 

# Input:  10->15->12->13->20->14,  x = 12, y = 20
# Output: 10->15->20->13->12->14

# Input:  10->15->12->13->20->14,  x = 10, y = 20
# Output: 20->15->12->13->10->14

# Input:  10->15->12->13->20->14,  x = 12, y = 13
# Output: 10->15->13->12->20->14

# This may look a simple problem, but is an interesting question as it has the following cases to be handled. 
# 1) x and y may or may not be adjacent. 
# 2) Either x or y may be a head node. 
# 3) Either x or y may be the last node. 
# 4) x and/or y may not be present in the linked list.

# The idea is to first search x and y in the given linked list. If any of them is not present, then return. While searching for x and y, keep track of current and previous pointers. First change next of previous pointers, then change next of current pointers. 

# Below is the implementation of the above approach. 
# Python program to swap two given nodes of a linked list 
class LinkedList(object): 
	def __init__(self): 
		self.head = None

	# head of list 
	class Node(object): 
		def __init__(self, d): 
			self.data = d 
			self.next = None

	# Function to swap Nodes x and y in linked list by 
	# changing links 
	def swapNodes(self, x, y): 

		# Nothing to do if x and y are same 
		if x == y: 
			return

		# Search for x (keep track of prevX and CurrX) 
		prevX = None
		currX = self.head 
		while currX != None and currX.data != x: 
			prevX = currX 
			currX = currX.next

		# Search for y (keep track of prevY and currY) 
		prevY = None
		currY = self.head 
		while currY != None and currY.data != y: 
			prevY = currY 
			currY = currY.next

		# If either x or y is not present, nothing to do 
		if currX == None or currY == None: 
			return
		# If x is not head of linked list 
		if prevX != None: 
			prevX.next = currY 
		else: #make y the new head 
			self.head = currY 

		# If y is not head of linked list 
		if prevY != None: 
			prevY.next = currX 
		else: # make x the new head 
			self.head = currX 

		# Swap next pointers 
		temp = currX.next
		currX.next = currY.next
		currY.next = temp 

	# Function to add Node at beginning of list. 
	def push(self, new_data): 

		# 1. alloc the Node and put the data 
		new_Node = self.Node(new_data) 

		# 2. Make next of new Node as head 
		new_Node.next = self.head 

		# 3. Move the head to point to new Node 
		self.head = new_Node 

	# This function prints contents of linked list starting 
	# from the given Node 
	def printList(self): 
		tNode = self.head 
		while tNode != None: 
			print(tNode.data,end=" ") 
			tNode = tNode.next

# Driver program to test above function 
llist = LinkedList() 

# The constructed linked list is: 
# 1->2->3->4->5->6->7 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 
print("Linked list before calling swapNodes() ")
llist.printList() 
llist.swapNodes(4, 3) 
print("\nLinked list after calling swapNodes() ")
llist.printList() 

# Optimizations: The above code can be optimized to search x and y in single traversal. Two loops are used to keep program simple.



# second method
# Simpler approach –

# Python3 program to swap two given 
# nodes of a linked list 

# A linked list node class 
class Node : 
	
	# constructor 
	def __init__(self, val = None, next1 = None): 
		self.data = val 
		self.next = next1 

	# print list from this 
	# to last till None 
	def printList(self): 
	
		node = self

		while (node != None) : 
			print(node.data, end = " ") 
			node = node.next
		print(" ") 
	
# Function to add a node 
# at the beginning of List 
def push(head_ref, new_data) : 

	# allocate node 
	(head_ref) = Node(new_data, head_ref) 
	return head_ref 

def swapNodes(head_ref, x, y) : 
	head = head_ref 
	
	# Nothing to do if x and y are same 
	if (x == y) : 
		return None

	a = None
	b = None

	# search for x and y in the linked list 
	# and store therir pointer in a and b 
	while (head_ref.next != None) : 

		if ((head_ref.next).data == x) : 
			a = head_ref 

		elif ((head_ref.next).data == y) : 
			b = head_ref 
		
		head_ref = ((head_ref).next) 
	

	# if we have found both a and b 
	# in the linked list swap current 
	# pointer and next pointer of these 
	if (a != None and b != None) : 
		temp = a.next
		a.next = b.next
		b.next = temp	 
		temp = a.next.next
		a.next.next = b.next.next
		b.next.next = temp 
	
	return head 

# Driver code 

start = None

# The constructed linked list is: 
# 1.2.3.4.5.6.7 
start = push(start, 7) 
start = push(start, 6) 
start = push(start, 5) 
start = push(start, 4) 
start = push(start, 3) 
start = push(start, 2) 
start = push(start, 1) 

print("Linked list before calling swapNodes() ") 
start.printList() 

start=swapNodes(start, 6, 3) 

print("Linked list after calling swapNodes() ") 
start.printList() 

