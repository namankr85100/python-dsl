# Given an array of integers, print the array in such a way that the first element is first maximum and second element is first minimum and so on.

# Examples :

# Input : arr[] = {7, 1, 2, 3, 4, 5, 6}
# Output : 7 1 6 2 5 3 4

# Input : arr[] = {1, 6, 9, 4, 3, 7, 8, 2}
# Output : 9 1 8 2 7 3 6 4

# A simple solution is to first print maximum element, then minimum, then second maximum, and so on. Time complexity of this approach is O(n2).

# An efficient solution involves following steps.
# 1) Sort input array using a O(n Log n) algorithm.
# 2) We maintain two pointers, one from beginning and one from end in sorted array. We alternatively print elements pointed by two pointers and move them toward each other.

# function to print alternative sorted
#values
def alternative(arr,n):

    #sorting the array
    arr.sort()

    #printing the last element of array
    #first and then first element and then
    #second last element and then second
    #element and so on
    i=0
    j=n-1

    while(i<j):
        print(arr[j],end=" ")
        j-=1
        print(arr[i],end=" ")
        i+=1

    #if the total element in array is odd
    #then print the last middle element
    if(n%2!=0):
        print(arr[i])

#driver code
arr=[1,12,4,6,7,10]
n=len(arr)
alternative(arr,n)

# time complexity :O(nlogn)
# auxiliary space:O(1)