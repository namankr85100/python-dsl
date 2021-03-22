# Merge Sort for Linked Lists

# Merge sort is often preferred for sorting a linked list. The slow random-access performance of a linked list makes some other algorithms (such as quicksort) perform poorly, and others (such as heapsort) completely impossible.
# sorting image

# Let head be the first node of the linked list to be sorted and headRef be the pointer to head. Note that we need a reference to head in MergeSort() as the below implementation changes next links to sort the linked lists (not data at the nodes), so head node has to be changed if the data at the original head is not the smallest value in the linked list.

# MergeSort(headRef)
# 1) If the head is NULL or there is only one element in the Linked List 
#     then return.
# 2) Else divide the linked list into two halves.  
#       FrontBackSplit(head, &a, &b); /* a and b are two halves */
# 3) Sort the two halves a and b.
#       MergeSort(a);
#       MergeSort(b);
# 4) Merge the sorted a and b (using SortedMerge() discussed here) 
#    and update the head pointer using headRef.
#      *headRef = SortedMerge(a, b);


# Python3 program to merge sort of linked list 

# create Node using class Node. 
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 
	def __init__(self): 
		self.head = None
	
	# push new value to linked list 
	# using append method 
	def append(self, new_value): 
		
		# Allocate new node 
		new_node = Node(new_value) 
		
		# if head is None, initialize it to new node 
		if self.head is None: 
			self.head = new_node 
			return
		curr_node = self.head 
		while curr_node.next is not None: 
			curr_node = curr_node.next
			
		# Append the new node at the end 
		# of the linked list 
		curr_node.next = new_node 
		
	def sortedMerge(self, a, b): 
		result = None
		
		# Base cases 
		if a == None: 
			return b 
		if b == None: 
			return a 
			
		# pick either a or b and recur.. 
		if a.data <= b.data: 
			result = a 
			result.next = self.sortedMerge(a.next, b) 
		else: 
			result = b 
			result.next = self.sortedMerge(a, b.next) 
		return result 
	
	def mergeSort(self, h): 
		
		# Base case if head is None 
		if h == None or h.next == None: 
			return h 

		# get the middle of the list 
		middle = self.getMiddle(h) 
		nexttomiddle = middle.next

		# set the next of middle node to None 
		middle.next = None

		# Apply mergeSort on left list 
		left = self.mergeSort(h) 
		
		# Apply mergeSort on right list 
		right = self.mergeSort(nexttomiddle) 

		# Merge the left and right lists 
		sortedlist = self.sortedMerge(left, right) 
		return sortedlist 
	
	# Utility function to get the middle 
	# of the linked list 
	def getMiddle(self, head): 
		if (head == None): 
			return head 

		slow = head 
		fast = head 

		while (fast.next != None and
			fast.next.next != None): 
			slow = slow.next
			fast = fast.next.next
			
		return slow 
		
# Utility function to print the linked list 
def printList(head): 
	if head is None: 
		print(' ') 
		return
	curr_node = head 
	while curr_node: 
		print(curr_node.data, end = " ") 
		curr_node = curr_node.next
	print(' ') 
	
# Driver Code 
if __name__ == '__main__': 
	li = LinkedList() 
	
	# Let us create a unsorted linked list 
	# to test the functions created. 
	# The list shall be a: 2->3->20->5->10->15 
	li.append(15) 
	li.append(10) 
	li.append(5) 
	li.append(20) 
	li.append(3) 
	li.append(2) 
	
	# Apply merge Sort 
	li.head = li.mergeSort(li.head) 
	print ("Sorted Linked List is:") 
	printList(li.head) 

# Time Complexity: O(n Log n)