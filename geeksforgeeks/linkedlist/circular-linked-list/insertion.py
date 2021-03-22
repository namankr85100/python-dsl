# Why Circular? In a singly linked list, for accessing any node of linked list, we start traversing from the first node. If we are at any node in the middle of the list, then it is not possible to access nodes that precede the given node. This problem can be solved by slightly altering the structure of singly linked list. In a singly linked list, next part (pointer to next node) is NULL, if we utilize this link to point to the first node then we can reach preceding nodes. Refer this for more advantages of circular linked lists.
# The structure thus formed is circular singly linked list look like this: 



# In this post, the implementation and insertion of a node in a Circular Linked List using singly linked list are explained.

# Implementation 
# To implement a circular singly linked list, we take an external pointer that points to the last node of the list. If we have a pointer last pointing to the last node, then last -> next will point to the first node. 






# The pointer last points to node Z and last -> next points to node P.

# Why have we taken a pointer that points to the last node instead of first node ? 
# For insertion of node in the beginning we need traverse the whole list. Also, for insertion at the end, the whole list has to be traversed. If instead of start pointer we take a pointer to the last node then in both the cases there won’t be any need to traverse the whole list. So insertion in the beginning or at the end takes constant time irrespective of the length of the list.

# Insertion 
# A node can be added in three ways: 

# Insertion in an empty list
# Insertion at the beginning of the list
# Insertion at the end of the list
# Insertion in between the nodes
# Insertion in an empty List 
# Initially, when the list is empty, last pointer will be NULL. 
 



# After inserting a node T, 
 






# After insertion, T is the last node so pointer last points to node T. And Node T is first and last node, so T is pointing to itself. 
# Function to insert node in an empty List, 

# filter_none
# edit
# play_arrow

# brightness_4

# c++
# struct Node *addToEmpty(struct Node *last, int data)
# {
# 	// This function is only for empty list
# 	if (last != NULL)
# 	return last;

# 	// Creating a node dynamically.
# 	struct Node *temp =
# 		(struct Node*)malloc(sizeof(struct Node));

# 	// Assigning the data.
# 	temp -> data = data;
# 	last = temp;
# 	// Note : list was empty. We link single node
# 	// to itself.
# 	temp -> next = last;

# 	return last;
# }


# Insertion at the beginning of the list 
# To Insert a node at the beginning of the list, follow these step: 
# 1. Create a node, say T. 
# 2. Make T -> next = last -> next. 
# 3. last -> next = T. 

# java

# static Node addBegin(Node last, int data)
# {
# 	if (last == null)
# 		return addToEmpty(last, data);

# 	// Creating a node dynamically
# 	Node temp = new Node();
	
# 	// Assigning the data
# 	temp.data = data;

# 	// Adjusting the links
# 	temp.next = last.next;
# 	last.next = temp;

# 	return last;
# }

# // This code is contributed by rutvik_56


# Insertion at the end of the list 
# To Insert a node at the end of the list, follow these step: 
# 1. Create a node, say T. 
# 2. Make T -> next = last -> next; 
# 3. last -> next = T. 
# 4. last = T. 

# struct Node *addEnd(struct Node *last, int data)
# {
# if (last == NULL)
# 	return addToEmpty(last, data);

# // Creating a node dynamically.
# struct Node *temp = 
# 		(struct Node *)malloc(sizeof(struct Node));

# // Assigning the data.
# temp -> data = data;

# // Adjusting the links.
# temp -> next = last -> next;
# last -> next = temp;
# last = temp;

# return last;
# }



# Insertion in between the nodes 
# To Insert a node in between the two nodes, follow these step: 
# 1. Create a node, say T. 
# 2. Search the node after which T need to be insert, say that node be P. 
# 3. Make T -> next = P -> next; 
# 4. P -> next = T.
# Suppose 12 need to be insert after node having value 10, 

# struct Node *addAfter(struct Node *last, int data, int item)
# {
# 	if (last == NULL)
# 	return NULL;

# 	struct Node *temp, *p;
# 	p = last -> next;

# 	// Searching the item.
# 	do
# 	{
# 		if (p ->data == item)
# 		{
# 			// Creating a node dynamically.
# 			temp = (struct Node *)malloc(sizeof(struct Node));

# 			// Assigning the data.
# 			temp -> data = data;

# 			// Adjusting the links.
# 			temp -> next = p -> next;

# 			// Adding newly allocated node after p.
# 			p -> next = temp;

# 			// Checking for the last node.
# 			if (p == last)
# 				last = temp;

# 			return last;
# 		}
# 		p = p -> next;
# 	} while (p != last -> next);

# 	cout << item << " not present in the list." << endl;
# 	return last;
# }


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.last = None

	# This function is only for empty list
	def addToEmpty(self, data):

		if (self.last != None):
			return self.last

		# Creating the newnode temp
		temp = Node(data)
		self.last = temp

		# Creating the link
		self.last.next = self.last
		return self.last

	def addBegin(self, data):

		if (self.last == None):
			return self.addToEmpty(data)

		temp = Node(data)
		temp.next = self.last.next
		self.last.next = temp

		return self.last

	def addEnd(self, data):

		if (self.last == None):
			return self.addToEmpty(data)

		temp = Node(data)
		temp.next = self.last.next
		self.last.next = temp
		self.last = temp

		return self.last

	def addAfter(self, data, item):

		if (self.last == None):
			return None

		temp = Node(data)
		p = self.last.next
		while p:
			if (p.data == item):
				temp.next = p.next
				p.next = temp

				if (p == self.last):
					self.last = temp
					return self.last
				else:
					return self.last
			p = p.next
			if (p == self.last.next):
				print(item, "not present in the list")
				break

	def traverse(self):
		if (self.last == None):
			print("List is empty")
			return

		temp = self.last.next
		while temp:
			print(temp.data, end = " ")
			temp = temp.next
			if temp == self.last.next:
				break

# Driver Code
if __name__ == '__main__':

	llist = CircularLinkedList()

	last = llist.addToEmpty(6)
	last = llist.addBegin(4)
	last = llist.addBegin(2)
	last = llist.addEnd(8)
	last = llist.addEnd(12)
	last = llist.addAfter(10,8)

	llist.traverse()

