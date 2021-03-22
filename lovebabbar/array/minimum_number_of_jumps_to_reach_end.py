# Python3 program to find Minimum 
# number of jumps to reach end

# Returns minimum number of jumps
# to reach arr[h] from arr[l]
def minJumps(arr, l, h):

	# Base case: when source and
	# destination are same
	if (h == l):
		return 0

	# when nothing is reachable 
	# from the given source
	if (arr[l] == 0):
		return float('inf')

	# Traverse through all the points 
	# reachable from arr[l]. Recursively 
	# get the minimum number of jumps 
	# needed to reach arr[h] from 
	# these reachable points.
	min = float('inf')
	for i in range(l + 1, h + 1):
		if (i < l + arr[l] + 1):
			jumps = minJumps(arr, i, h)
			if (jumps != float('inf') and
					jumps + 1 < min):
				min = jumps + 1

	return min

# Driver program to test above function
arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
n = len(arr)
print('Minimum number of jumps to reach',
	'end is', minJumps(arr, 0, n-1))

# This code is contributed by Soumen Ghosh








# Python3 progrma to find Minimum 
# number of jumps to reach end

# Returns Minimum number of
# jumps to reach end
def minJumps(arr, n):
	
	# jumps[0] will hold the result
	jumps = [0 for i in range(n)] 

	# Minimum number of jumps needed
	# to reach last element from 
	# last elements itself is always 0
	# jumps[n-1] is also initialized to 0

	# Start from the second element, 
	# move from right to left and 
	# construct the jumps[] array where
	# jumps[i] represents minimum number
	# of jumps needed to reach arr[m-1]
	# form arr[i]
	for i in range(n-2, -1, -1):
		
		# If arr[i] is 0 then arr[n-1]
		# can't be reached from here
		if (arr[i] == 0):
			jumps[i] = float('inf')

		# If we can directly reach to 
		# the end point from here then
		# jumps[i] is 1
		elif (arr[i] >= n - i - 1):
			jumps[i] = 1

		# Otherwise, to find out the 
		# minimum number of jumps
		# needed to reach arr[n-1], 
		# check all the points
		# reachable from here and 
		# jumps[] value for those points
		else:
			# initialize min value
			min = float('inf') 

			# following loop checks with 
			# all reachavle points and
			# takes the minimum
			for j in range(i + 1, n):
				if (j <= arr[i] + i):
					if (min > jumps[j]):
						min = jumps[j]
						
			# Handle overflow
			if (min != float('inf')):
				jumps[i] = min + 1
			else:
				# or INT_MAX
				jumps[i] = min

	return jumps[0]

# Driver program to test above function
arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
n = len(arr)
print('Minimum number of jumps to reach',
	'end is', minJumps(arr, n-1))
	
# This code is contributed by Soumen Ghosh
