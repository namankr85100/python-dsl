# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
from sys import maxint
def maxSubArraySum(a1,size):
	
	max_so_far = -maxint - 1
	max_ending_here = 0
	
	for i in range(0, size):
		max_ending_here = max_ending_here + a1[i]
		if (max_so_far < max_ending_here):
			max_so_far = max_ending_here

		if max_ending_here < 0:
			max_ending_here = 0
	return max_so_far

# Driver function to check the above function 
a1 = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print "Maximum contiguous sum is", maxSubArraySum(a1,len(a1))

#This code is contributed by _Devesh Agrawal_





def maxSubArraySum(a,size):
	
	max_so_far = 0
	max_ending_here = 0
	
	for i in range(0, size):
		max_ending_here = max_ending_here + a[i]
		if max_ending_here < 0:
			max_ending_here = 0
		
		# Do not compare for all elements. Compare only 
		# when max_ending_here > 0
		elif (max_so_far < max_ending_here):
			max_so_far = max_ending_here
			
	return max_so_far





# Python program to find maximum contiguous subarray

def maxSubArraySum(a,size):
	
	max_so_far =a[0]
	curr_max = a[0]
	
	for i in range(1,size):
		curr_max = max(a[i], curr_max + a[i])
		max_so_far = max(max_so_far,curr_max)
		
	return max_so_far

# Driver function to check the above function 
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print"Maximum contiguous sum is" , maxSubArraySum(a,len(a))

#This code is contributed by _Devesh Agrawal_





# Python program to print largest contiguous array sum

from sys import maxsize

# Function to find the maximum contiguous subarray
# and print its starting and end index
def maxSubArraySum(a,size):

	max_so_far = -maxsize - 1
	max_ending_here = 0
	start = 0
	end = 0
	s = 0

	for i in range(0,size):

		max_ending_here += a[i]

		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
			start = s
			end = i

		if max_ending_here < 0:
			max_ending_here = 0
			s = i+1

	print ("Maximum contiguous sum is %d"%(max_so_far))
	print ("Starting Index %d"%(start))
	print ("Ending Index %d"%(end))

# Driver program to test maxSubArraySum
a = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSubArraySum(a,len(a))
