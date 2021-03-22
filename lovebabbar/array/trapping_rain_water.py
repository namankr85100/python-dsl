# Python3 implementation of the approach 

# Function to return the maximum 
# water that can be stored 
def maxWater(arr, n) :
	
	# To store the maximum water 
	# that can be stored 
	res = 0; 
	
	# For every element of the array 
	for i in range(1, n - 1) : 
		
		# Find the maximum element on its left 
		left = arr[i]; 
		for j in range(i) :
			left = max(left, arr[j]); 
		
		# Find the maximum element on its right 
		right = arr[i]; 
		
		for j in range(i + 1 , n) : 
			right = max(right, arr[j]);
			
		# Update the maximum water
		res = res + (min(left, right) - arr[i]); 

	return res; 

# Driver code 
if __name__ == "__main__" : 

	arr = [0, 1, 0, 2, 1, 0, 
		1, 3, 2, 1, 2, 1]; 
	n = len(arr); 
	
	print(maxWater(arr, n)); 
	
# This code is contributed by AnkitRai01





# Python program to find maximum amount of water that can
# be trapped within given set of bars.

def findWater(arr, n):

	# left[i] contains height of tallest bar to the
	# left of i'th bar including itself
	left = [0]*n

	# Right [i] contains height of tallest bar to
	# the right of ith bar including itself
	right = [0]*n

	# Initialize result
	water = 0

	# Fill left array
	left[0] = arr[0]
	for i in range( 1, n):
		left[i] = max(left[i-1], arr[i])

	# Fill right array
	right[n-1] = arr[n-1]
	for i in range(n-2, -1, -1):
		right[i] = max(right[i + 1], arr[i]);

	# Calculate the accumulated water element by element
	# consider the amount of water on i'th bar, the
	# amount of water accumulated on this particular
	# bar will be equal to min(left[i], right[i]) - arr[i] .
	for i in range(0, n):
		water += min(left[i], right[i]) - arr[i]

	return water


# Driver program

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
print("Maximum water that can be accumulated is", findWater(arr, n))

# This code is contributed by
# Smitha Dinesh Semwal
