# input : arr[] ={15,18,2,3,6,12}
# output:2
# explanation:initial array must be (2,3,6,12,15,18),we get the 
# given array after rotating the initial array twice

# input:arr[]={7,9,11,12,5}
# output:4

# input:arr[] ={7,9,11,12,5}
# output:4

# input :arr[]={7,9,11,12,15}
# output:0

# Method 1 (Using linear search)

# If we take closer look at examples, we can notice that the number of rotations is equal to index of minimum element. A simple linear solution is to find minimum element and returns its index. 

# program to find a number of rotation in a sorted and rotated array

# returns count od rotation for
# an array which is first sorted 
# in ascending order,then rotated
def countrotations(arr,n):

    #we basically find index
    #of minimum element
    min = arr[0]
    for i in range(0,n):
        if (min>arr[i]):
            min = arr[i]
            min_index=i
    return min_index
arr=[15,18,2,3,6,12]
n=len(arr)
print(countrotations(arr,n))

# time complexity:O(n)
# auxiliary space:O(1)


# second method
# Method 2 (Efficient Using Binary Search)
# Here also we find the index of minimum element, but using Binary Search. The idea is based on the below facts :

# The minimum element is the only element whose previous is greater than it. If there is no previous element, then there is no rotation (first element is minimum). We check this condition for middle element by comparing it with (mid-1)’th and (mid+1)’th elements.
# If the minimum element is not at the middle (neither mid nor mid + 1), then minimum element lies in either left half or right half.
# If middle element is smaller than last element, then the minimum element lies in left half
# Else minimum element lies in right half.

# returns count of rotation to handle the case when array
# is not rotated at all

def countrotation(arr,low,high):

    #this condition is needed to handle the case when array
    # is not rotated at all
    if (high < low):
        return 0
    
    #if there is only one element left
    if(high ==low):
        return low

    #find mid (low+high)/2
    mid= low+(high-low)/2
    mid =int(mid)

    #check if element (mid+1) is minimum element .consider
    #the cases like{3,4,5,1,2}
    if(mid<high and arr[mid+1]<arr[mid]):
        return (mid+1)
    
    #check if mid itself is minimum element
    if(mid>low and arr[mid]<arr[mid-1]):
        return mid

    #decide whether we need to go to left half or right half
    if(arr[high]>arr[mid]):
        return countrotation(arr,low,mid-1)

    return countrotation(arr,mid+1,high)

arr=[15,18,2,3,6]
n=len(arr)
print(countrotation(arr,0,n-1))
# time complexity:O(logn)
# auxiliary space:O(1)