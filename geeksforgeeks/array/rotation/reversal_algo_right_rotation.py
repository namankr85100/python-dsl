# Input: arr[] = {1, 2, 3, 4, 5, 
#                 6, 7, 8, 9, 10}
#           k = 3
# Output: 8 9 10 1 2 3 4 5 6 7

# Input: arr[] = {121, 232, 33, 43 ,5}
#            k = 2
# Output: 43 5 121 232 33

# Note : In the below solution, k is assumed to be smaller than or equal to n.
#  We can easily modify the solutions to handle larger k values by doing k = k % n

# rotate(arr[], d, n)
#   reverseArray(arr[], 0, n-1) 
#   reverse(arr[], 0, d-1)
#   reverse(arr[], d, n-1)

# function to reverse arr
# from index start to end
def reversearray(ar,start,end):
    while(start < end):
        arr[start],arr[end]=arr[end],arr[start]
        start = start+1
        end = end-1

# function to right rotate arr
#of size  n by d
def rightrotate(arr,d,n):
    reversearray(arr,0,n-1)
    reversearray(arr,0,d-1)
    reversearray(arr,d,n-1)

#function to print an array
def prarray(arr,size):
    for i in range(0,size):
        print(arr[i],end=" ")

#driver code
arr=[1,2,3,4,5,6,7,8,9,10]
n=len(arr)
k=3

#function call
rightrotate(arr,k,n)
prarray(arr,n)
