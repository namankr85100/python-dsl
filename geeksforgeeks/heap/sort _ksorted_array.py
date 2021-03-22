"""Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.
Examples: 
 

Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
            k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
         k = 4
Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}
 """

def insertionsort(a,size):
    i,key,j=0,0,0
    for i in range(size):
        key=a[i]
        j=i-1

        #move elements of a[0..i-1],that are
        #grater than key,to one position
        #ahead of their current position
        #this loop will run at most k times
        while(j>=0 and a[j]>key):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
"""
The Min Heap based method takes O(nLogk) time and uses O(k) auxiliary space. 
We can also use a Balanced Binary Search Tree instead of Heap to store K+1 elements. The insert and delete operations on Balanced BST also take O(Logk) time. So Balanced BST based method will also take O(nLogk) time, but the Heap bassed method seems to be more efficient as the minimum element will always be at root. Also, Heap doesn’t need extra space for left and right pointers.
Please write comments if you find any of the above codes/algorithms incorrect, or find other ways to solve the same problem.
 """