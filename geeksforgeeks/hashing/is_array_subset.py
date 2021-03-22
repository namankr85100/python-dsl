"""
Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[] or not. Both the arrays are not in sorted order. It may be assumed that elements in both array are distinct.

Examples: 

Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1} 
Output: arr2[] is a subset of arr1[]

Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4} 
Output: arr2[] is a subset of arr1[]

Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3} 
Output: arr2[] is not a subset of arr1[] 




Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution. 
 
Method 1 (Simple): 
Use two loops: The outer loop picks all the elements of arr2[] one by one. The inner loop linearly searches for the element picked by the outer loop. If all elements are found then return 1, else return 0.
"""
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

#Time Complexity: O(m*n)
"""
Method 2 (Use Sorting and Binary Search):  

Sort arr1[] which takes O(mLogm)
For each element of arr2[], do binary search for it in sorted arr1[].
If the element is not found then return 0.
If all elements are present then return 1."""

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

# Time Complexity: O(mLogm + nLogm). Please note that this will be the complexity if an mLogm algorithm is used for sorting which is not the case in above code. In above code Quick Sort is used and worst case time complexity of Quick Sort is O(m^2)


#Method 3 (Use Sorting and Merging ) 
"""
Sort both arrays: arr1[] and arr2[] which takes O(mLogm + nLogn)
Use Merge type of process to see if all elements of sorted arr2[] are present in sorted arr1[].
Thanks to Parthsarthi for suggesting this method.
Below image is a dry run of the above approach:"""

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
	print("arr2 is not a subset of arr1 ")

#Time Complexity: O(mLogm + nLogn) which is better than method 2. Please note that this will be the complexity if an nLogn algorithm is used for sorting both arrays which is not the case in above code. In above code Quick Sort is used and worst case time complexity of Quick Sort is O(n^2)


"""Method 4 (Use Hashing)  

Create a Hash Table for all the elements of arr1[].
Traverse arr2[] and search for each element of arr2[] in the Hash Table. If element is not found then return 0.
If all elements are found then return 1."""
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


#Method 5 (Use Set)
"""
Insert into the set for the first array; that’s how we will know the elements in the array.
Save the size of the array after inserting the first array element.
Insert into the same set for the second array.
Check if the size of the set is still the same or not, if it is then it’s true else false."""

"""include <bits/stdc++.h>
using namespace std;

int main()
{
	// code
	int arr1[] = { 11, 1, 13, 21, 3, 7 };
	int arr2[] = { 11, 3, 7, 1 };
	int m = sizeof(arr1) / sizeof(arr1[0]);
	int n = sizeof(arr2) / sizeof(arr2[0]);
	unordered_set<int> s;
	for (int i = 0; i < m; i++) {
		s.insert(arr1[i]);
	}
	int p = s.size();
	for (int i = 0; i < n; i++) {
		s.insert(arr2[i]);
	}
	if (s.size() == p) {
	cout << "arr2[] is subset of arr1[] "
			<< "\n";
	}
	else {
		cout << "arr2[] is not subset of arr1[] "
			<< "\n";
	}
	return 0;
}"""

# Time Complexity: O(m+n) because we are using unordered_set and inserting in it, If we would be using a ordered set inserting would have taken 


#Method 6 (Use Frequency Table)  
"""
Create a Frequency Table for all the elements of arr1[].
Traverse arr2[] and search for each element of arr2[] in the Frequency Table. if element is found decrease the frequency, If element frequency is not found then return 0.
If all elements are found then return 1."""


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

#Note that method 1, method 2 and method 4 don’t handle the cases when we have duplicates in arr2[]. For example, {1, 4, 4, 2} is not a subset of {1, 4, 2}, but these methods will print it as a subset.  

# Time Complexity: O(m+n) which is better than method 1,2,3.