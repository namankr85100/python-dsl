# Given an array of size n and multiple values around which we need to left rotate the array. How to quickly find multiple left rotations?

# Examples:

# Input : arr[] = {1, 3, 5, 7, 9}
#         k1 = 1
#         k2 = 3
#         k3 = 4
#         k4 = 6
# Output : 3 5 7 9 1
#          7 9 1 3 5
#          9 1 3 5 7
#          3 5 7 9 1

# Input : arr[] = {1, 3, 5, 7, 9}
#         k1 = 14
# Output : 9 1 3 5 7

# Simple Approach: We have already discussed different approaches in below posts.

# Left Rotation of array (Simple and Juggling Algorithms).
# Block swap algorithm for array rotation
# Reversal algorithm for array rotation
# The best of above approaches take O(n) time and O(1) extra space


# Efficient Approach:
# The above approaches work well when there is single rotation required. The approaches also modify the original array. To handle multiple queries of array rotation, we use a temp array of size 2n and quickly handle rotations.

# Step 1 : Copy the entire array two times in temp[0..2n-1] array.
# Step 2 : Starting position of array after k rotations in temp[] will be k % n. We do k
# Step 3 : Print temp[] array from k % n to k % n + n.

def preprocess(arr, n):
    temp = [None]*(2*n)

    # store arr elements at i and i + n
    for i in range(n):
        temp[i] = temp[i+n] = arr[i]
    return temp


def leftrotate(arr, n, k, temp):

    # starting postion of array after k
    # rotation in temp will be k % n
    start = k % n

    # print array after k rotations
    for i in range(start, start+n):
        print(temp[i], end=" ")
    print("")


# driver program
arr = [1, 3, 5, 7, 9]
n = len(arr)
temp = preprocess(arr, n)

k = 2
leftrotate(arr, n, k, temp)

k = 3
leftrotate(arr, n, k, temp)

k = 4
leftrotate(arr, n, k, temp)

# Note that the task to find starting address of rotation takes O(1) time.
# It is printing the elements that takes O(n) time.

# Space optimized Approach : The above method takes extra space.
# Below given is the space optimized solution.

print("")
def leftrotate(arr, n, k):

    # print array
    # after k rotations
    for i in range(k, k+n):
        print(str(arr[i % n]), end=" ")

# driver code
arr=[1, 3, 5, 6, 9]
n=len(arr)
k=2
leftrotate(arr, n, k)
print()

k=3
leftrotate(arr, n, k)
print()

k=4
leftrotate(arr, n, k)
print()
