# A Python3 program to print elements with
# count more than n/k

# Prints elements with more than n/k
# occurrences in arrof size n. If
# there are no such elements, then
# it prints nothing.


def moreThanNdK(arr, n, k):

	# k must be greater than 1
	# to get some output
	if (k < 2):
		return

	# Step 1: Create a temporary array
	# (contains element and count) of
	# size k-1. Initialize count of all
	# elements as 0
	temp = [[0 for i in range(2)]
			for i in range(k)]

	for i in range(k - 1):
		temp[i][0] = 0

	# Step 2: Process all elements
	# of input array
	for i in range(n):
		j = 0

		# If arr[i] is already present in
		# the element count array, then
		# increment its count
		while j < k - 1:
			if (temp[j][1] == arr[i]):
				temp[j][0] += 1
				break

			j += 1

		# If arr[i] is not present in temp
		if (j == k - 1):
			l = 0

			# If there is position available
			# in temp[], then place arr[i]
			# in the first available position
			# and set count as 1*/
			while l < k - 1:
				if (temp[l][0] == 0):
					temp[l][1] = arr[i]
					temp[l][0] = 1
					break

				l += 1

			# If all the position in the
			# tempare filled, then decrease
			# count of every element by 1
			if (l == k - 1):
				while l < k:
					temp[l][0] -= 1
					l += 1

	# Step 3: Check actual counts
	# of potential candidates in temp[]
	for i in range(k - 1):

		# Calculate actual count of elements
		ac = 0 # Actual count
		for j in range(n):
			if (arr[j] == temp[i][1]):
				ac += 1

		# If actual count is more
		# than n/k, then prit
		if (ac > n // k):
			print("Number:",
				temp[i][1],
				" Count:", ac)


# Driver code
if __name__ == '__main__':

	print("First Test")
	arr1 = [4, 5, 6, 7, 8, 4, 4]
	size = len(arr1)
	k = 3
	moreThanNdK(arr1, size, k)

	print("Second Test")
	arr2 = [4, 2, 2, 7]
	size = len(arr2)
	k = 3
	moreThanNdK(arr2, size, k)

	print("Third Test")
	arr3 = [2, 7, 2]
	size = len(arr3)
	k = 2
	moreThanNdK(arr3, size, k)

	print("Fourth Test")
	arr4 = [2, 3, 3, 2]
	size = len(arr4)
	k = 3
	moreThanNdK(arr4, size, k)

# This code is contributed by mohit kumar 29




# second
# Python3 code to find elements whose 
# frequency yis more than n/k 
def morethanNbyK(arr, n, k) :
	x = n // k
	
	# unordered_map initialization
	freq = {}

	for i in range(n) : 
		if arr[i] in freq :
			freq[arr[i]] += 1
		else :
			freq[arr[i]] = 1
		
	# Traversing the map
	for i in freq :
		
		# Checking if value of a key-value pair
		# is greater than x (where x=n/k)
		if (freq[i] > x) :
			
			# Print the key of whose value
			# is greater than x
			print(i)

# Driver code		 
arr = [ 1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1 ]
n = len(arr)
k = 4

morethanNbyK(arr, n, k)

# This code is contributed by mohit kumar 29
