"""
Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in S whose sum is exactly x. 

Examples: 

Input: arr[] = {0, -1, 2, -3, 1}
        sum = -2
Output: -3, 1
If we calculate the sum of the output,
1 + (-3) = -2

Input: arr[] = {1, -2, 1, 0, 5}
       sum = 0
Output: -1
No valid pair exists.


Method 1: Sorting and Two-Pointers technique.

Approach: A tricky approach to solve this problem can be to use the two-pointer technique. But for using two pointer technique, the array must be sorted. Once the array is sorted the two pointers can be taken which mark the beginning and end of the array respectively. If the sum is greater than the sum of those two elements, shift the left pointer to increase the value of required sum and if the sum is lesser than the required value, shift the right pointer to decrease the value. Let’s understand this using an example.

Let an array be {1, 4, 45, 6, 10, -8} and sum to find be 16
After sorting the array 
A = {-8, 1, 4, 6, 10, 45}
Now, increment ‘l’ when the sum of the pair is less than the required sum and decrement ‘r’ when the sum of the pair is more than the required sum. 
This is because when the sum is less than the required sum then to get the number which could increase the sum of pair, start moving from left to right(also sort the array) thus “l++” and vice versa.
Initialize l = 0, r = 5 
A[l] + A[r] ( -8 + 45) > 16 => decrement r. Now r = 4 
A[l] + A[r] ( -8 + 10) increment l. Now l = 1 
A[l] + A[r] ( 1 + 10) increment l. Now l = 2 
A[l] + A[r] ( 4 + 10) increment l. Now l = 3 
A[l] + A[r] ( 6 + 10) == 16 => Found candidates (return 1)




Note: If there is more than one pair having the given sum then this algorithm reports only one. Can be easily extended for this though. 

Algorithm: 

hasArrayTwoCandidates (A[], ar_size, sum)
Sort the array in non-decreasing order.
Initialize two index variables to find the candidate 
elements in the sorted array. 
Initialize first to the leftmost index: l = 0
Initialize second the rightmost index: r = ar_size-1
Loop while l < r. 
If (A[l] + A[r] == sum) then return 1
Else if( A[l] + A[r] < sum ) then l++
Else r–
No candidates in the whole array – return 0

"""
# condition to be satisified

def hasArrayTwoCandidates(A, arr_size, sum):
	
	# sort the array
	quickSort(A, 0, arr_size-1)
	l = 0
	r = arr_size-1
	
	# traverse the array for the two elements
	while l<r:
		if (A[l] + A[r] == sum):
			return 1
		elif (A[l] + A[r] < sum):
			l += 1
		else:
			r -= 1
	return 0

# Implementation of Quick Sort
# A[] --> Array to be sorted
# si --> Starting index
# ei --> Ending index
def quickSort(A, si, ei):
	if si < ei:
		pi = partition(A, si, ei)
		quickSort(A, si, pi-1)
		quickSort(A, pi + 1, ei)

# Utility function for partitioning 
# the array(used in quick sort)
def partition(A, si, ei):
	x = A[ei]
	i = (si-1)
	for j in range(si, ei):
		if A[j] <= x:
			i += 1
			
			# This operation is used to swap 
			# two variables is python
			A[i], A[j] = A[j], A[i]

		A[i + 1], A[ei] = A[ei], A[i + 1]
		
	return i + 1
	

# Driver program to test the functions
A = [1, 4, 45, 6, 10, -8]
n = 16
if (hasArrayTwoCandidates(A, len(A), n)):
	print("Array has two elements with the given sum")
else:
	print("Array doesn't have two elements 	with the given sum")

# Complexity Analysis:  

# Time Complexity: Depends on what sorting algorithm we use. 
# If Merge Sort or Heap Sort is used then (-)(nlogn) in the worst case.
# If Quick Sort is used then O(n^2) in the worst case.
# Auxiliary Space: This too depends on sorting algorithm. The auxiliary space is O(n) for merge sort and O(1) for Heap Sort.


#hashing
"""Method 2: Hashing.

Approach: This problem can be solved efficiently by using the technique of hashing. Use a hash_map to check for the current array value x(let), if there exists a value target_sum-x which on adding to the former gives target_sum. This can be done in constant time. Let’s look at the following example. 

arr[] = {0, -1, 2, -3, 1} 
sum = -2 
Now start traversing: 
Step 1: For ‘0’ there is no valid number ‘-2’ so store ‘0’ in hash_map. 
Step 2: For ‘-1’ there is no valid number ‘-1’ so store ‘-1’ in hash_map. 
Step 3: For ‘2’ there is no valid number ‘-4’ so store ‘2’ in hash_map. 
Step 4: For ‘-3’ there is no valid number ‘1’ so store ‘-3’ in hash_map. 
Step 5: For ‘1’ there is a valid number ‘-3’ so answer is 1, -3 

Algorithm:  




Initialize an empty hash table s.
Do following for each element A[i] in A[] 
If s[x – A[i]] is set then print the pair (A[i], x – A[i])
Insert A[i] into s.
Pseudo Code :  

unordered_set s
for(i=0 to end)
  if(s.find(target_sum - arr[i]) == s.end)
    insert(arr[i] into s)
  else 
    print arr[i], target-arr[i]"""

# Python program to find if there are
# two elements wtih given sum

# function to check for the given sum
# in the array
def printPairs(arr, arr_size, sum):
	
	# Create an empty hash set
	s = set()
	
	for i in range(0, arr_size):
		temp = sum-arr[i]
		if (temp in s):
			print ("Pair with given sum "+ str(sum) +
	" is (" + str(arr[i]) + ", " + str(temp) + ")")
		s.add(arr[i])

# driver code
A = [1, 4, 45, 6, 10, 8]
n = 16
printPairs(A, len(A), n)

"""
Complexity Analysis:  

Time Complexity: O(n). 
As the whole array is needed to be traversed only once.
Auxiliary Space: O(n). 
A hash map has been used to store array elements."""


""" 
Method 3: Using remainders of the elements less than x. 

Approach: 
The idea is to count the elements with remainders when divided by x, i.e 0 to x-1, each remainder separately. Suppose we have x as 6, then the numbers which are less than 6 and have remainders which add up to 6 gives sum as 6 when added. For example, we have elements, 2,4 in the array and 2%6 = 2 and 4%6 =4, and these remainders add up to give 6. Like that we have to check for pairs with remainders (1,5),(2,4),(3,3). if we have one or more elements with remainder 1 and one or more elements with remainder 5, then surely we get a sum as 6. Here we do not consider (0,6) as the elements for the resultant pair should be less than 6. when it comes to (3,3) we have to check if we have two elements with remainder 3, then we can say that “There exists a pair whose sum is x”. 

Algorithm:  

1. Create an array with size x. 

2. Initialize all rem elements to zero.

3. Traverse the given array

Do the following if arr[i] is less than x:
r=arr[i]%x which is done to get the remainder.
rem[r]=rem[r]+1 i.e. increasing the count of elements that have remainder r when divided with x.
4. Now, traverse the rem array from 1 to x/2.   

If(rem[i]> 0 and rem[x-i]>0) then print “YES” and come out of the loop. This means that we have a pair that results in x upon doing.
5. Now when we reach at x/2 in the above loop   

If x is even, for getting a pair we should have two elements with remainder x/2.
If rem[x/2]>1 then print “YES” else print “NO”
If it is not satisfied that is x is odd, it will have a separate pair with x-x/2.
If rem[x/2]>1 and rem[x-x/2]>1 , then print “Yes” else, print”No”
"""
# exists a pair in array whose
# sum results in x.

# Funtion to print pairs
def printPairs(a, n, x):
	
	rem = []
	
	for i in range(x):

		# Initializing the rem
		# values with 0's.
		rem.append(0)

	for i in range(n):
		if (a[i] < x):

			# Perform the remainder operation
			# only if the element is x, as 
			# numbers greater than x can't
			# be used to get a sum x.Updating
			# the count of remainders.
			rem[a[i] % x] += 1

	# Traversing the remainder list from
	# start to middle to find pairs
	for i in range(1, x // 2):
		if (rem[i] > 0 and rem[x - i] > 0):

			# The elements with remainders
			# i and x-i will result to a 
			# sum of x. Once we get two
			# elements which add up to x,
			# we print x and break.
			print("Yes")
			break

	# Once we reach middle of
	# remainder array, we have to
	# do operations based on x.
	if (i >= x // 2):
		if (x % 2 == 0):
			if (rem[x // 2] > 1):

				# If x is even and we have more
				# than 1 elements with remainder
				# x/2, then we will have two 
				# distinct elements which add up
				# to x. if we dont have than 1
				# element, print "No".
				print("Yes")
			else:
				print("No")
		else:

			# When x is odd we continue
			# the same process which we
			# did in previous loop.
			if (rem[x // 2] > 0 and
				rem[x - x // 2] > 0):
				print("Yes")
			else:
				print("No")

# Driver Code
A = [ 1, 4, 45, 6, 10, 8 ]
n = 16
arr_size = len(A)

# Function calling
printPairs(A, arr_size, n)


"""
Time Complexity: O(n+x)
Auxiliary Space: O(x)
Related Problems:  """
