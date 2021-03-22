# Python 3 program to find whether an array
# is subset of another array

# Return 1 if arr2[] is a subset of 
# arr1[] 
def isSubset(arr1, arr2, m, n):
	i = 0
	j = 0
	for i in range(n):
		for j in range(m):
			if(arr2[i] == arr1[j]):
				break
		
		# If the above inner loop was
		# not broken at all then arr2[i]
		# is not present in arr1[] 
		if (j == m):
			return 0
	
	# If we reach here then all
	# elements of arr2[] are present
	# in arr1[] 
	return 1

# Driver code
if __name__ == "__main__":
	
	arr1 = [11, 1, 13, 21, 3, 7]
	arr2 = [11, 3, 7, 1]

	m = len(arr1)
	n = len(arr2)

	if(isSubset(arr1, arr2, m, n)):
		print("arr2[] is subset of arr1[] ")
	else:
		print("arr2[] is not a subset of arr1[]")

# This code is contributed by ita_c




# Python3 program to find whether an array
# is subset of another array

# Return 1 if arr2[] is a subset of arr1[]


def isSubset(arr1, arr2, m, n):
	i = 0

	quickSort(arr1, 0, m-1)
	for i in range(n):
		if (binarySearch(arr1, 0, m - 1, arr2[i]) == -1):
			return 0

	# If we reach here then all elements
	# of arr2[] are present in arr1[]
	return 1

# FOLLOWING FUNCTIONS ARE ONLY FOR
# SEARCHING AND SORTING PURPOSE
# Standard Binary Search function


def binarySearch(arr, low, high, x):
	if(high >= low):
		mid = (low + high)//2

		# Check if arr[mid] is the first 
		# occurrence of x.
		# arr[mid] is first occurrence if x is 
		# one of the following
		# is true:
		# (i) mid == 0 and arr[mid] == x
		# (ii) arr[mid-1] < x and arr[mid] == x
		if((mid == 0 or x > arr[mid-1]) and (arr[mid] == x)):
			return mid
		elif(x > arr[mid]):
			return binarySearch(arr, (mid + 1), high, x)
		else:
			return binarySearch(arr, low, (mid - 1), x)

	return -1


def partition(A, si, ei):
	x = A[ei]
	i = (si - 1)

	for j in range(si, ei):
		if(A[j] <= x):
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i + 1], A[ei] = A[ei], A[i + 1]
	return (i + 1)

# Implementation of Quick Sort
# A[] --> Array to be sorted
# si --> Starting index
# ei --> Ending index


def quickSort(A, si, ei):
	# Partitioning index
	if(si < ei):
		pi = partition(A, si, ei)
		quickSort(A, si, pi - 1)
		quickSort(A, pi + 1, ei)


# Driver code
arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

m = len(arr1)
n = len(arr2)

if(isSubset(arr1, arr2, m, n)):
	print("arr2[] is subset of arr1[] ")
else:
	print("arr2[] is not a subset of arr1[] ")


# This code is contributed by chandan_jnu





# Python3 program to find whether an array
# is subset of another array

# Return 1 if arr2[] is a subset of arr1[] */


def isSubset(arr1, arr2, m, n):
	i = 0
	j = 0
	if m < n:
		return 0

	arr1.sort()
	arr2.sort()

	while i < n and j < m:
		if arr1[j] < arr2[i]:
			j += 1
		elif arr1[j] == arr2[i]:
			j += 1
			i += 1
		elif arr1[j] > arr2[i]:
			return 0
	return False if i < n else True


# Driver code
arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

m = len(arr1)
n = len(arr2)
if isSubset(arr1, arr2, m, n) == True:
	print("arr2 is subset of arr1 ")
else:
	printf("arr2 is not a subset of arr1 ")

# This code is contributed by Shrikant13


# Python3 program to find whether an array
# is subset of another array

# Return true if arr2[] is a subset
# of arr1[]
def isSubset(arr1, m, arr2, n):
	
	# Using STL set for hashing
	hashset = set()

	# hset stores all the values of arr1
	for i in range(0, m):
		hashset.add(arr1[i])

	# Loop to check if all elements
	# of arr2 also lies in arr1
	for i in range(0, n):
		if arr2[i] in hashset:
			continue
		else:
			return False

	return True

# Driver Code
if __name__ == '__main__':
	
	arr1 = [ 11, 1, 13, 21, 3, 7 ] 
	arr2 = [ 11, 3, 7, 1 ]
	
	m = len(arr1)
	n = len(arr2)
	
	if (isSubset(arr1, m, arr2, n)):
		print("arr2[] is subset of arr1[] ")
	else:
		print("arr2[] is not a subset of arr1[] ")

# This code is contributed by akhilsaini





# Python3 code
arr1 = [ 11, 1, 13, 21, 3, 7 ]
arr2 = [ 11, 3, 7, 1 ]
m = len(arr1) 
n = len(arr2) 
s = set()
for i in range(m) :
	s.add(arr1[i])

p = len(s)
for i in range(n) :
	s.add(arr2[i])

if (len(s) == p) :
	print("arr2[] is subset of arr1[] ")

else :
	print("arr2[] is not subset of arr1[] ")
	
	# This code is contributed by divyeshrabadiya07.



# Python3 program to find whether an array
# is subset of another array

# Return true if arr2[] is a subset of arr1[]
def isSubset(arr1, m, arr2, n):
	
	# Create a Frequency Table using STL
	frequency = {}

	# Increase the frequency of each element
	# in the frequency table.
	for i in range(0, m):
		if arr1[i] in frequency:
			frequency[arr1[i]] = frequency[arr1[i]] + 1
		else:
			frequency[arr1[i]] = 1

	# Decrease the frequency if the
	# element was found in the frequency
	# table with the frequency more than 0.
	# else return 0 and if loop is
	# completed return 1.
	for i in range(0, n):
		if (frequency[arr2[i]] > 0):
			frequency[arr2[i]] -= 1
		else:
			return False

	return True

# Driver Code
if __name__ == '__main__':
	
	arr1 = [ 11, 1, 13, 21, 3, 7 ]
	arr2 = [ 11, 3, 7, 1 ]
	
	m = len(arr1)
	n = len(arr2)

	if (isSubset(arr1, m, arr2, n)):
		print("arr2[] is subset of arr1[] ")
	else:
		print("arr2[] is not a subset of arr1[] ")

# This code is contributed by akhilsaini
