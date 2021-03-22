# O(logn) only in binary search
# input:arr[]={5,6,7,8,9,10,1,2,3}
# key=3
# output:found at index 8
# input:arr[]={5,6,7,8,9,10,1,2,3}
# key=30
# output:not found

# implementaion
# input arr[] = {3,4,5,1,2}
# element to search = 1
# 1)find out pivot point and divide the array in two
# sub-arrays.(pivot =2)
# 2)now call binary search for one of the two sub-arrays
#  (a) if element is greter than 0th elment then
#     searc in left array
#  (b)else search in right array
#     (1 will go in else as 1 < 0th element(3))
# 3)if element is found in selected sub-array then return Index
# else return -1    

# in a sorted and pivoted array
# searches an element key in a pivoted
#sorted array arr[] of size n
def pivotedbinarysearch(arr,n,key):
    pivot = findpivot(arr,0,n-1)

    #if we couldnot find a pivot
    #then array is not rotated at all
    if pivot == -1:
        return binarysearch(arr,0,n-1,key)
    
    #if we found a pivot , then first
    #compare with pivot and then
    #search in two subarrays around pivot
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binarysearch(arr,0,pivot-1,key)
    return binarysearch(arr,pivot+1,n-1,key)

    #function to get pivot .for array
    #3,4,5,6,1,2 it returns 3
    #(index of 6)
def findpivot(arr,low,high):
        #base cases
        if high <low:
            return -1
        if high == low:
            return low
        #low +(high-low)/2
        mid = int((low+high)/2)

        if (mid < high and arr[mid]>arr[mid+1]):
            return mid
        if (mid > low and arr[mid] < arr[mid -1]):
            return (mid-1)
        if(arr[low] >= arr[mid]):
            return findpivot(arr,low,mid-1)
        return findpivot(arr,mid+1,high)

def binarysearch(arr,low,high,key):
    if(high < low):
        return -1
    #low + (high-low)/2
    mid = int((low+high)/2)

    if(key == arr[mid]):
        return mid
    if(key > arr[mid]):
        return binarysearch(arr,(mid+1),high,key)
    return binarysearch(arr,low,(mid-1),key)

arr=[5,6,7,8,9,10,1,2,3]
n=len(arr)
key=3
print("index of the element is",pivotedbinarysearch(arr,n,key))
# time complexity:O(logn)
# space complexity:O(1)    



# -----------------
# second method
# approach :
# instead of two or more pass of binary search the result 
# can be found in one pass of binary search .the binary search needs to be modified
# to perform that search .the idea is to create a recursive function
# that takes l and r as range in input and the key

# 1.find middle point mid=(l+h)/2
# 2.if key is present at middle point ,return mid
# 3.else if arr[l..mid] is sorted
#     a.if key to be searched lies in range from arr[l]
#     to arr[mid], recur for arr[l..mid]
#     b.else recur for arr[mid+1..h]
# 4.else (arr[mid+1..h] must be sorted)
#     a.if key to be searched lies in range from arr[mid+1]
#     to arr[h],recur for arr[mid+1..h]
#     b.else recur for arr[l..mid]    
    
#returns index of key in arr[l..h] i key is present
# Search an element in sorted and rotated array using 
# single pass of Binary Search 

# Returns index of key in arr[l..h] if key is present, 
# otherwise returns -1 
def search (arr, l, h, key): 
	if l > h: 
		return -1
	
	mid = (l + h) / 2
	if arr[mid] == key: 
		return mid 

	# If arr[l...mid] is sorted 
	if arr[l] <= arr[mid]: 

		# As this subarray is sorted, we can quickly 
		# check if key lies in half or other half 
		if key >= arr[l] and key <= arr[mid]: 
			return search(arr, l, mid-1, key) 
		return search(arr, mid + 1, h, key) 

	# If arr[l..mid] is not sorted, then arr[mid... r] 
	# must be sorted 
	if key >= arr[mid] and key <= arr[h]: 
		return search(a, mid + 1, h, key) 
	return search(arr, l, mid-1, key) 

# Driver program 
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
key = 6
i = search(arr, 0, len(arr)-1, key) 
if i != -1: 
	print ("Index: % d"% i) 
else: 
	print ("Key not found") 

# time complexity :O(logn)
# auxiliary space:O(1)