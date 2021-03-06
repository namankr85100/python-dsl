# Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

# Always pick first element as pivot.
# Always pick last element as pivot (implemented below)
# Pick a random element as pivot.
# Pick median as pivot.
# The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

# Pseudo Code for recursive QuickSort function :
# /* low  --> Starting index,  high  --> Ending index */
# quickSort(arr[], low, high)
# {
#     if (low < high)
#     {
#         /* pi is partitioning index, arr[pi] is now
#            at right place */
#         pi = partition(arr, low, high);

#         quickSort(arr, low, pi - 1);  // Before pi
#         quickSort(arr, pi + 1, high); // After pi
#     }
# }

# Partition Algorithm
# There can be many ways to do partition, following pseudo code adopts the method given in CLRS book. The logic is simple, we start from the leftmost element and keep track of index of smaller (or equal to) elements as i. While traversing, if we find a smaller element, we swap current element with arr[i]. Otherwise we ignore current element.

# /* low  --> Starting index,  high  --> Ending index */
# quickSort(arr[], low, high)
# {
#     if (low < high)
#     {
#         /* pi is partitioning index, arr[pi] is now
#            at right place */
#         pi = partition(arr, low, high);

#         quickSort(arr, low, pi - 1);  // Before pi
#         quickSort(arr, pi + 1, high); // After pi
#     }
# }


# Partition Algorithm
# There can be many ways to do partition, following pseudo code adopts the method given in CLRS book. The logic is simple, we start from the leftmost element and keep track of index of smaller (or equal to) elements as i. While traversing, if we find a smaller element, we swap current element with arr[i]. Otherwise we ignore current element.

# /* low  --> Starting index,  high  --> Ending index */
# quickSort(arr[], low, high)
# {
#     if (low < high)
#     {
#         /* pi is partitioning index, arr[pi] is now
#            at right place */
#         pi = partition(arr, low, high);

#         quickSort(arr, low, pi - 1);  // Before pi
#         quickSort(arr, pi + 1, high); // After pi
#     }
# }



# Illustration of partition() :

# arr[] = {10, 80, 30, 90, 40, 50, 70}
# Indexes:  0   1   2   3   4   5   6 

# low = 0, high =  6, pivot = arr[h] = 70
# Initialize index of smaller element, i = -1

# Traverse elements from j = low to high-1
# j = 0 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
# i = 0 
# arr[] = {10, 80, 30, 90, 40, 50, 70} // No change as i and j 
#                                      // are same

# j = 1 : Since arr[j] > pivot, do nothing
# // No change in i and arr[]

# j = 2 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
# i = 1
# arr[] = {10, 30, 80, 90, 40, 50, 70} // We swap 80 and 30 

# j = 3 : Since arr[j] > pivot, do nothing
# // No change in i and arr[]

# j = 4 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
# i = 2
# arr[] = {10, 30, 40, 90, 80, 50, 70} // 80 and 40 Swapped
# j = 5 : Since arr[j] <= pivot, do i++ and swap arr[i] with arr[j] 
# i = 3 
# arr[] = {10, 30, 40, 50, 80, 90, 70} // 90 and 50 Swapped 

# We come out of loop because j is now equal to high-1.
# Finally we place pivot at correct position by swapping
# arr[i+1] and arr[high] (or pivot) 
# arr[] = {10, 30, 40, 50, 70, 90, 80} // 80 and 70 Swapped 

# Now 70 is at its correct place. All elements smaller than
# 70 are before it and all elements greater than 70 are after
# it.

# Implementation:
# Following are the implementations of QuickSort:

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
	i = ( low-1 )		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		# If current element is smaller than the pivot 
		if arr[j] < pivot: 
		
			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low,high): 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i],end= " "), 

# Analysis of QuickSort
# Time taken by QuickSort in general can be written as following.

#  T(n) = T(k) + T(n-k-1) + \theta(n)