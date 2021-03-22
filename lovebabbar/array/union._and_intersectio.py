# Python3 program of the 
# above approach

# Function to shift all the 
# the negative elements to
# the left of the array
def shiftall(arr,left,right):

# Loop to iterate while the 
# left pointer is less than
# the right pointer
while left<=right:
	
	# Condition to check if the left
	# and right pointer negative
	if arr[left] < 0 and arr[right] < 0:
	left+=1
	
	# Condition to check if the left 
	# pointer element is positive and 
	# the right pointer element is
	# negative
	elif arr[left]>0 and arr[right]<0:
	arr[left], arr[right] = \
			arr[right],arr[left]
	left+=1
	right-=1
	
	# Condition to check if the left
	# pointer is positive and right 
	# pointer as well
	elif arr[left]>0 and arr[right]>0:
	right-=1
	else:
	left+=1
	right-=1
	
# Function to print the array
def display(arr):
for i in range(len(arr)):
	print(arr[i], end=" ")
print()

# Driver Code
if __name__ == "__main__":
arr=[-12, 11, -13, -5, \
	6, -7, 5, -3, 11]
n=len(arr)
shiftall(arr,0,n-1)
display(arr)

# Sumit Singh








# Python3 program to find union of two 
# sorted arrays (Handling Duplicates) 
def UnionArray(arr1, arr2): 
	
	# Taking max element present in either array 
	m = arr1[-1] 
	n = arr2[-1] 
	ans = 0
		
	if m > n: 
		ans = m 
	else: 
		ans = n 
		
	# Finding elements from 1st array 
	# (non duplicates only). Using 
	# another array for storing union 
	# elements of both arrays 
	# Assuming max element present 
	# in array is not more than 10 ^ 7 
	newtable = [0] * (ans + 1) 
		
	# First element is always 
	# present in final answer 
	print(arr1[0], end = " ") 
		
	# Incrementing the First element's count 
	# in it's corresponding index in newtable 
	newtable[arr1[0]] += 1
		
	# Starting traversing the first 
	# array from 1st index till last 
	for i in range(1, len(arr1)): 
		
		# Checking whether current element 
		# is not equal to it's previous element 
		if arr1[i] != arr1[i - 1]: 
			
			print(arr1[i], end = " ") 
			newtable[arr1[i]] += 1
			
	# Finding only non common 
	# elements from 2nd array		 
	for j in range(0, len(arr2)): 
		
		# By checking whether it's already 
		# present in newtable or not 
		if newtable[arr2[j]] == 0: 
			
			print(arr2[j], end = " ") 
			newtable[arr2[j]] += 1
	
# Driver Code 
if __name__ == "__main__": 
	
	arr1 = [1, 2, 2, 2, 3] 
	arr2 = [2, 3, 4, 5] 
		
	UnionArray(arr1, arr2) 

# This code is contributed by Rituraj Jain 




# Python program to find intersection of 
# two sorted arrays 
# Function prints Intersection of arr1[] and arr2[] 
# m is the number of elements in arr1[] 
# n is the number of elements in arr2[] 
def printIntersection(arr1, arr2, m, n): 
	i, j = 0, 0
	while i < m and j < n: 
		if arr1[i] < arr2[j]: 
			i += 1
		elif arr2[j] < arr1[i]: 
			j+= 1
		else: 
			print(arr2[j]) 
			j += 1
			i += 1

# Driver program to test above function 
arr1 = [1, 2, 4, 5, 6] 
arr2 = [2, 3, 5, 7] 
m = len(arr1) 
n = len(arr2) 
printIntersection(arr1, arr2, m, n) 

# This code is contributed by Pratik Chhajer 




# Python3 program to find Intersection of two 
# Sorted Arrays (Handling Duplicates) 
def IntersectionArray(a, b, n, m): 
	''' 
	:param a: given sorted array a 
	:param n: size of sorted array a 
	:param b: given sorted array b 
	:param m: size of sorted array b 
	:return: array of intersection of two array or -1 
	'''

	Intersection = [] 
	i = j = 0
	
	while i < n and j < m: 
		if a[i] == b[j]: 

			# If duplicate already present in Intersection list 
			if len(Intersection) > 0 and Intersection[-1] == a[i]: 
				i+= 1
				j+= 1

			# If no duplicate is present in Intersection list 
			else: 
				Intersection.append(a[i]) 
				i+= 1
				j+= 1
		elif a[i] < b[j]: 
			i+= 1
		else: 
			j+= 1
			
	if not len(Intersection): 
		return [-1] 
	return Intersection 

# Driver Code 
if __name__ == "__main__": 

	arr1 = [1, 2, 2, 3, 4] 
	arr2 = [2, 2, 4, 6, 7, 8] 
	
	l = IntersectionArray(arr1, arr2, len(arr1), len(arr2)) 
	print(*l) 

# This code is contributed by Abhishek Kumar 
