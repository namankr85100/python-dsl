# example:
# Input : 
# arr[] = {1, 3, 5, 7, 9}
# k1 = 1
# k2 = 3
# k3 = 4
# k4 = 6
# Output : 
# 3 5 7 9 1
# 7 9 1 3 5
# 9 1 3 5 7
# 3 5 7 9 1

# Input : 
# arr[] = {1, 3, 5, 7, 9}
# k1 = 14 
# Output : 
# 9 1 3 5 7

# method1
# The solution discussed above requires extra space. In this post,
#  an optimized solution is discussed that doesn’t require extra space.

#left rotation of array k number of times

def leftrotate(arr,n,k):

    #to get the starting point of rotated array
    mod = k%n
    s=""

    #prints the rotated array from start position
    for i in range(n):
        print(str(arr[(mod+i)%n]),end=" ")

arr =[1,3,5,7,9]
n=len(arr)
k=2

#function call
leftrotate(arr,n,k)

# method 2:
# In the below implementation we will use Standard Template Library (STL) 
# which will be making the solution more optimize and easy to Implement.

# print left rotation of any array k times
from collections import deque
def leftrotate(arr,k,n):

    #the collections module has deque class
    #which provides the rotate(),which is
    #inbuilt function to allow rotation
    arr=deque(arr)

    #using rotate() to left rotate by k
    arr.rotate(-k)
    arr=list(arr)

    #print the rotated array from
    #start position
    for i in range(n):
        print(arr[i],end=" ")

arr=[1,3,5,7,9]
n= len(arr)
k=2
print("\nsecond method")
leftrotate(arr,k,n)