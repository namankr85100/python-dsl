# Write a function detectAndRemoveLoop() that checks whether a given Linked List contains loop and if loop is present then removes the loop and returns true. 
# If the list doesn’t contain loop then it returns false.
#  Below diagram shows a linked list with a loop. detectAndRemoveLoop() must change the below list to 1->2->3->4->5->NULL.

# Before trying to remove the loop, we must detect it. Techniques discussed in the above post can be used to detect loop. To remove loop, all we need to do is to get pointer to the last node of the loop. For example,
#  node with value 5 in the above diagram. Once we have pointer to the last node,
#  we can make the next of this node as NULL and loop is gone. 
# We can easily use Hashing or Visited node techniques (discussed in the above mentioned post) to get the pointer to the last node. Idea is simple: the very first node whose next is already visited (or hashed) is the last node. 
# We can also use Floyd Cycle Detection algorithm to detect and remove the loop. In the Floyd’s algo, the slow and fast pointers meet at a loop node. We can use this loop node to remove cycle. 
# There are following two different ways of removing loop when Floyd’s algorithm is used for Loop detection.

# Method 1 (Check one by one) We know that Floyd’s Cycle detection algorithm terminates when fast and slow pointers meet at a common point. We also know that this common point is one of the loop nodes (2 or 3 or 4 or 5 in the above diagram).
#  Store the address of this in a pointer variable say ptr2.
#  After that start from the head of the Linked List and check for nodes one by one if they are reachable from ptr2. Whenever we find a node that is reachable, 
# we know that this node is the starting node of the loop in Linked List and we can get the pointer to the previous of this node.

# Python program to detect and remove loop in linked list

# Node class


class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	def detectAndRemoveLoop(self):
		slow_p = fast_p = self.head
		while(slow_p and fast_p and fast_p.next):
			slow_p = slow_p.next
			fast_p = fast_p.next.next

			# If slow_p and fast_p meet at some poin
			# then there is a loop
			if slow_p == fast_p:
				self.removeLoop(slow_p)

				# Return 1 to indicate that loop if found
				return 1

		# Return 0 to indicate that there is no loop
		return 0

	# Function to remove loop
	# loop node-> Pointer to one of the loop nodes
	# head --> Pointer to the start node of the
	# linked list
	def removeLoop(self, loop_node):

		# Set a pointer to the beginning of the linked
		# list and move it one by one to find the first
		# node which is part of the linked list
		ptr1 = self.head
		while(1):
			# Now start a pointer from loop_node and check
			# if it ever reaches ptr2
			ptr2 = loop_node
			while(ptr2.next != loop_node and ptr2.next != ptr1):
				ptr2 = ptr2.next

			# If ptr2 reached ptr1 then there is a loop.
			# So break the loop
			if ptr2.next == ptr1:
				break

			ptr1 = ptr1.next

		# After the end of loop ptr2 is the lsat node of
		# the loop. So make next of ptr2 as NULL
		ptr2.next = None
	# Function to insert a new node at the beginning

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to prit the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data,end=" ")
			temp = temp.next


# Driver code
llist = LinkedList()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)

# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next

llist.detectAndRemoveLoop()

print("Linked List after removing loop")
llist.printList()


# # better solutiom
# Method 2 (Better Solution)  

# This method is also dependent on Floyd’s Cycle detection algorithm.
# Detect Loop using Floyd’s Cycle detection algorithm and get the pointer to a loop node.
# Count the number of nodes in loop. Let the count be k.
# Fix one pointer to the head and another to a kth node from the head.
# Move both pointers at the same pace, they will meet at loop starting node.
# Get a pointer to the last node of the loop and make next of it as NULL

# Python program to detect and remove loop in linked list

# Node class 
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	def detectAndRemoveLoop(self):
		slow_p = fast_p = self.head
		
		while(slow_p and fast_p and fast_p.next):
			slow_p = slow_p.next
			fast_p = fast_p.next.next

			# If slow_p and fast_p meet at some point then
			# there is a loop
			if slow_p == fast_p:
				self.removeLoop(slow_p)
		
				# Return 1 to indicate that loop is found
				return 1
		
		# Return 0 to indicate that there is no loop
		return 0

	# Function to remove loop
	# loop_node --> pointer to one of the loop nodes
	# head --> Pointer to the start node of the linked list
	def removeLoop(self, loop_node):
		ptr1 = loop_node
		ptr2 = loop_node
		
		# Count the number of nodes in loop
		k = 1
		while(ptr1.next != ptr2):
			ptr1 = ptr1.next
			k += 1

		# Fix one pointer to head
		ptr1 = self.head
		
		# And the other pointer to k nodes after head
		ptr2 = self.head
		for i in range(k):
			ptr2 = ptr2.next

		# Move both pointers at the same place
		# they will meet at loop starting node
		while(ptr2 != ptr1):
			ptr1 = ptr1.next
			ptr2 = ptr2.next

		# Get pointer to the last node
		while(ptr2.next != ptr1):
			ptr2 = ptr2.next

		# Set the next node of the loop ending node
		# to fix the loop
		ptr2.next = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data,end=" ")
			temp = temp.next


# Driver program
llist = LinkedList()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)

# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next

llist.detectAndRemoveLoop()

print("Linked List after removing loop")
llist.printList()


# Method 3 (Optimized Method 2: Without Counting Nodes in Loop) 
# We do not need to count number of nodes in Loop. After detecting the loop, if we start slow pointer from head and move both slow and fast pointers at same speed until fast don’t meet, they would meet at the beginning of the loop.
# How does this work? 
# Let slow and fast meet at some point after Floyd’s Cycle finding algorithm. Below diagram shows the situation when cycle is found.


# Distance traveled by fast pointer = 2 * (Distance traveled 
#                                          by slow pointer)

# (m + n*x + k) = 2*(m + n*y + k)

# Note that before meeting the point shown above, fast
# was moving at twice speed.

# x -->  Number of complete cyclic rounds made by 
#        fast pointer before they meet first time

# y -->  Number of complete cyclic rounds made by 
#        slow pointer before they meet first time
# From above equation, we can conclude below 

#     m + k = (x-2y)*n

# Which means m+k is a multiple of n. 
# Thus we can write, m + k = i*n or m = i*n - k.
# Hence, distance moved by slow pointer: m, is equal to distance moved by fast pointer:
# i*n - k or (i-1)*n + n - k (cover the loop completely i-1 times and start from n-k).


# So if we start moving both pointers again at same speed such that one pointer (say slow) begins from head node of linked list and other pointer (say fast) begins from meeting point. When slow pointer reaches beginning of loop (has made m steps), fast pointer would have made also moved m steps as they are now moving same pace. Since m+k is a multiple of n and fast starts from k, they would meet at the beginning. Can they meet before also? No because slow pointer enters the cycle first time after m steps. 

# fil

# Python program to detect and remove loop

# Node class


class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def detectAndRemoveLoop(self):

		if self.head is None:
			return
		if self.head.next is None:
			return

		slow = self.head
		fast = self.head

		# Move slow and fast 1 and 2 steps respectively
		slow = slow.next
		fast = fast.next.next

		# Search for loop using slow and fast pointers
		while (fast is not None):
			if fast.next is None:
				break
			if slow == fast:
				break
			slow = slow.next
			fast = fast.next.next

		# if loop exists
		if slow == fast:
			slow = self.head
			while (slow.next != fast.next):
				slow = slow.next
				fast = fast.next

			# Sinc fast.next is the looping point
			fast.next = None # Remove loop

	# Utility function to print the linked LinkedList

	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data,end=" ")
			temp = temp.next


# Driver program
llist = LinkedList()
llist.head = Node(50)
llist.head.next = Node(20)
llist.head.next.next = Node(15)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(10)

# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next

llist.detectAndRemoveLoop()

print ("Linked List after removing loop")
llist.printList()


