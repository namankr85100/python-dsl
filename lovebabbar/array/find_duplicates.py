# Python code to find the 
# repeated elements in the 
# array where every other
# is present once

# Function to find duplicate
def findDuplicate(arr):

	# Find the intersection 
	# point of the slow and fast.
	slow = arr[0]
	fast = arr[0]
	while True:
		slow = arr[slow]
		fast = arr[arr[fast]]
		if slow == fast:
			break

	# Find the "entrance"
	# to the cycle.
	ptr1 = arr[0]
	ptr2 = slow
	while ptr1 != ptr2:
		ptr1 = arr[ptr1]
		ptr2 = arr[ptr2]
		
	return ptr1
	
# Driver code
if __name__ == '__main__':
	
	
	arr = [ 1, 3, 2, 1 ]

	print(findDuplicate(arr))


# This code is contributed
# by Harshit Saini 
