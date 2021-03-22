# Merge two sorted linked lists

# Write a SortedMerge() function that takes two lists, each of which is sorted in increasing order, and merges the two together into one list which is in increasing order. SortedMerge() should return the new list. The new list should be made by splicing together the nodes of the first two lists.
# For example if the first linked list a is 5->10->15 and the other linked list b is 2->3->20, then SortedMerge() should return a pointer to the head node of the merged list 2->3->5->10->15->20.
# There are many cases to deal with: either ‘a’ or ‘b’ may be empty, during processing either ‘a’ or ‘b’ may run out first, and finally, there’s the problem of starting the result list empty, and building it up while going through ‘a’ and ‘b’.

# Method 1 (Using Dummy Nodes) 
# The strategy here uses a temporary dummy node as the start of the result list. The pointer Tail always points to the last node in the result list, so appending new nodes is easy. 
# The dummy node gives the tail something to point to initially when the result list is empty. This dummy node is efficient, since it is only temporary, and it is allocated in the stack. The loop proceeds, removing one node from either ‘a’ or ‘b’, and adding it to the tail. When 
# We are done, the result is in dummy.next. 
# The below image is a dry run of the above approach:

""" Python program to merge two
sorted linked lists """


# Linked List Node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


# Create & Handle List operations
class LinkedList:
	def __init__(self):
		self.head = None

	# Method to display the list
	def printList(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next

	# Method to add element to list
	def addToList(self, newData):
		newNode = Node(newData)
		if self.head is None:
			self.head = newNode
			return

		last = self.head
		while last.next:
			last = last.next

		last.next = newNode


# Function to merge the lists
# Takes two lists which are sorted
# joins them to get a single sorted list
def mergeLists(headA, headB):

	# A dummy node to store the result
	dummyNode = Node(0)

	# Tail stores the last node
	tail = dummyNode
	while True:

		# If any of the list gets completely empty
		# directly join all the elements of the other list
		if headA is None:
			tail.next = headB
			break
		if headB is None:
			tail.next = headA
			break

		# Compare the data of the lists and whichever is smaller is
		# appended to the last of the merged list and the head is changed
		if headA.data <= headB.data:
			tail.next = headA
			headA = headA.next
		else:
			tail.next = headB
			headB = headB.next

		# Advance the tail
		tail = tail.next

	# Returns the head of the merged list
	return dummyNode.next


# Create 2 lists
listA = LinkedList()
listB = LinkedList()

# Add elements to the list in sorted order
listA.addToList(5)
listA.addToList(10)
listA.addToList(15)

listB.addToList(2)
listB.addToList(3)
listB.addToList(20)

# Call the merge function
listA.head = mergeLists(listA.head, listB.head)

# Display merged list
print("Merged Linked List is:")
listA.printList()
