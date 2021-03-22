# # Delete a node in a Doubly Linked List
# Approach: The deletion of a node in a doubly linked list can be divided into three main categories: 

# After the deletion of the head node. 





# After the deletion of the middle node. 


# After the deletion of the last node.


# All three mentioned cases can be handled in two steps if the pointer of the node to be deleted and the head pointer is known. 

# If the node to be deleted is the head node then make the next node as head.
# If a node is deleted, connect the next and previous node of the deleted node. 


# Algorithm 

# Let the node to be deleted be del.
# If node to be deleted is head node, then change the head pointer to next current head. 
# if headnode == del then
#       headnode =  del.nextNode
# Set next of previous to del, if previous to del exists. 
# if del.nextNode != none 
#       del.nextNode.previousNode = del.previousNode 
# Set prev of next to del, if next to del exists.
# if del.previousNode != none 
#       del.previousNode.nextNode = del.next

# Program to delete a node in a doubly-linked list

# for Garbage collection
import gc

# A node of the doublly linked list
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data 
		self.next = None
		self.prev = None

class DoublyLinkedList:
	# Constructor for empty Doubly Linked List
	def __init__(self):
		self.head = None

# Function to delete a node in a Doubly Linked List.
# head_ref --> pointer to head node pointer.
# dele --> pointer to node to be deleted

	def deleteNode(self, dele):
		
		# Base Case
		if self.head is None or dele is None:
			return
		
		# If node to be deleted is head node
		if self.head == dele:
			self.head = dele.next

		# Change next only if node to be deleted is NOT
		# the last node
		if dele.next is not None:
			dele.next.prev = dele.prev
	
		# Change prev only if node to be deleted is NOT 
		# the first node
		if dele.prev is not None:
			dele.prev.next = dele.next
		# Finally, free the memory occupied by dele
		# Call python garbage collector
		gc.collect()


	# Given a reference to the head of a list and an
	# integer, inserts a new node on the front of list
	def push(self, new_data):

		# 1. Allocates node
		# 2. Put the data in it
		new_node = Node(new_data)

		# 3. Make next of new node as head and
		# previous as None (already None)
		new_node.next = self.head

		# 4. change prev of head node to new_node
		if self.head is not None:
			self.head.prev = new_node

		# 5. move the head to point to the new node
		self.head = new_node


	def printList(self, node):
		while(node is not None):
			print(node.data,end=" ")
			node = node.next


# Driver program to test the above functions

# Start with empty list
dll = DoublyLinkedList()

# Let us create the doubly linked list 10<->8<->4<->2
dll.push(2);
dll.push(4);
dll.push(8);
dll.push(10);

print("\n Original Linked List",end=" ")
dll.printList(dll.head)

# delete nodes from doubly linked list
dll.deleteNode(dll.head)
dll.deleteNode(dll.head.next)
dll.deleteNode(dll.head.next)
# Modified linked list will be NULL<-8->NULL
print("\n Modified Linked List",end=" ")
dll.printList(dll.head)

# Complexity Analysis: 

# Time Complexity: O(1). 
# Since traversal of the linked list is not required so the time complexity is constant.
# Space Complexity: O(1). 
# As no extra space is required, so the space complexity is constant.