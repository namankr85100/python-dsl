# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
# Example:
# First Pass:
# ( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
# ( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
# ( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
# ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

# Second Pass:
# ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
# ( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
# Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

# Third Pass:
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

def bubblesort(arr):
    n=len(arr)

    #traverse through all array elements
    for i in range(n):

        #last i elements are already in place
        for j in range(0,n-i-1):

            #traverse the array from 0 to n-1
            #swap if the element found is greater
            #then the next element
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

#driver code to test above
arr=[64,34,25,12,22,11,90]
bubblesort(arr)
print("sorted array is:")
for i in range(len(arr)):
    print(arr[i],end=" ")

# time complexity:O(n)
# The above function always runs O(n^2) time even if the array is sorted.
#  It can be optimized by stopping the algorithm if inner loop didn’t cause any swap.


# method 2:
# An optimized version of Bubble Sort 
def bubbleSort(arr): 
    n = len(arr) 
   
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already 
        #  in place 
        for j in range(0, n-i-1): 
   
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break
           
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
   
bubbleSort(arr) 
print()   
print ("Sorted array :") 
for i in range(len(arr)): 
    print ("%d" %arr[i],end=" ")

# Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

# Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

# Auxiliary Space: O(1)

# Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.    