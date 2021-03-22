class Node:

    #function to initialize the node object
    def __init__(self):
        self.data = data #assign data
        self.next = None #initialize next as null

class LinkedList:

    #function to initialize the Linked List object
    def __init__(self):
        self.head = None



# Add a node at the front: (4 steps process) 
# The new node is always added before the head of the given Linked List.
# And newly added node becomes the new head of the Linked List. 
# For example if the given Linked List is 10->15->20->25 and we add an item 5 at the front,
# then the Linked List becomes 5->10->15->20->25. Let us call the function that adds at the front of the list is push().
# The push() must receive a pointer to the head pointer,
# because push must change the head pointer to point to the new node 


# function to insert a new node at the beginning
def push(self,new_data):

    #1 & 2:allocate the Node &
    #     put in the data
    new_node =Node(new_data)

    #3.Make next of new Node as head
    new_node.next = self.head

    #4.Move the head to point to new Node
    self.head  = new_node

    # Time complexity of push() is O(1) as it does constant amount of work.

# Add a node after a given node: (5 steps process) 
# We are given pointer to a node, and the new node is inserted after the given node

def insertafter(Self,prev_node,new_data):
    #1.check if the given prev_node exists
    if prev_node is None:
        print ("this given previous node must inlinkedlist")
        return
    #2.create new node &
    #3.put in the data
    new_node =Node(new_data)

    #4 make next of new node as next of prev_node
    new_node.next = prev_node.next

    #5. make next of prev_node as new_node
    prev_node.next = new_node


# Add a node at the end: (6 steps process) 
# The new node is always added after the last node of the given Linked List. 
# For example if the given Linked List is 5->10->15->20->25 and we add an item 30 at the end, 
# then the Linked List becomes 5->10->15->20->25->30. 
# Since a Linked List is typically represented by the head of it, 
# we have to traverse the list till end and then change the next of last node to new node.

# Following are the 6 steps to add node at the end.

def append(self,new_data):
    #1.create a new node
    #2. put in the data
    #3. set next as None
    new_node = Node(new_data)

    #4. if the linked list is empty ,then make the 
    #nre node as head
    if self.head is None:
        self.head = new_node
        return
    
    #5.else traverse till the last node
    last = self.head
    while last.next:
        last = last.next
    
    #6.change the next of last node
    last.next = new_node

# Time complexity of append is O(n) where n is the number of nodes in linked list.
# Since there is a loop from head to end, the function does O(n) work. 
# This method can also be optimized to work in O(1) by keeping an extra pointer to tail of linked list/

# Following is a complete program that uses all of the above methods to create a linked list.
# A complete working Python program to demonstrate all 
# insertion methods of linked list 

# Node class 
class Node: 

	# Function to initialise the node object 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next = None # Initialize next as null 


# Linked List class contains a Node object 
class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None


	# Functio to insert a new node at the beginning 
	def push(self, new_data): 

		# 1 & 2: Allocate the Node & 
		#	 Put in the data 
		new_node = Node(new_data) 

		# 3. Make next of new Node as head 
		new_node.next = self.head 

		# 4. Move the head to point to new Node 
		self.head = new_node 


	# This function is in LinkedList class. Inserts a 
	# new node after the given prev_node. This method is 
	# defined inside LinkedList class shown above */ 
	def insertAfter(self, prev_node, new_data): 

		# 1. check if the given prev_node exists 
		if prev_node is None: 
			print ("The given previous node must inLinkedList.")
			return

		# 2. create new node & 
		#	 Put in the data 
		new_node = Node(new_data) 

		# 4. Make next of new Node as next of prev_node 
		new_node.next = prev_node.next

		# 5. make next of prev_node as new_node 
		prev_node.next = new_node 


	# This function is defined in Linked List class 
	# Appends a new node at the end. This method is 
	# defined inside LinkedList class shown above */ 
	def append(self, new_data): 

		# 1. Create a new node 
		# 2. Put in the data 
		# 3. Set next as None 
		new_node = Node(new_data) 

		# 4. If the Linked List is empty, then make the 
		# new node as head 
		if self.head is None: 
			self.head = new_node 
			return

		# 5. Else traverse till the last node 
		last = self.head 
		while (last.next): 
			last = last.next

		# 6. Change the next of last node 
		last.next = new_node 


	# Utility function to print the linked list 
	def printList(self): 
		temp = self.head 
		while (temp): 
			print (temp.data,end=" ") 
			temp = temp.next



# Code execution starts here 
if __name__=='__main__': 

	# Start with the empty list 
	llist = LinkedList() 

	# Insert 6. So linked list becomes 6->None 
	llist.append(6) 

	# Insert 7 at the beginning. So linked list becomes 7->6->None 
	llist.push(7); 

	# Insert 1 at the beginning. So linked list becomes 1->7->6->None 
	llist.push(1); 

	# Insert 4 at the end. So linked list becomes 1->7->6->4->None 
	llist.append(4) 

	# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
	llist.insertAfter(llist.head.next, 8) 

	print ('Created linked list is:',end=" ") 
	llist.printList() 
