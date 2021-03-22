# find maximum value of sum (i*arr[i]) with only rotation on given array allowed
# input:arr[]=(1,20,2,10)
# output:72
# # we can get 72 by rotating array twice
# (2,10,1,20)
# 20*3+1*2+10*1+2*0+72

# input:arr[]=(10,1,2,3,4,5,6,7,8,9)
# output:330
# we can get 330 by rotating array 9 times
# (1,2,3,4,5,6,7,8,9,10)
# # 0*1+1*2+2*3...9*10=330

# We strongly recommend you to minimize your browser and try this yourself first.
# A Simple Solution is to find all rotations one by one, check sum of every rotation and return the maximum sum. Time complexity of this solution is O(n2). 

# We can solve this problem in O(n) time using an Efficient Solution. 
# Let Rj be value of i*arr[i] with j rotations. The idea is to calculate next rotation value from previous rotation, i.e., calculate Rj from Rj-1. We can calculate initial value of result as R0, then keep calculating next rotation values. 

# How to efficiently calculate Rj from Rj-1? 
# This can be done in O(1) time. Below are details.  

# Let us calculate initial value of i*arr[i] with no rotation
# R0 = 0*arr[0] + 1*arr[1] +...+ (n-1)*arr[n-1]

# After 1 rotation arr[n-1], becomes first element of array, 
# arr[0] becomes second element, arr[1] becomes third element
# and so on.
# R1 = 0*arr[n-1] + 1*arr[0] +...+ (n-1)*arr[n-2]

# R1 - R0 = arr[0] + arr[1] + ... + arr[n-2] - (n-1)*arr[n-1]

# After 2 rotations arr[n-2], becomes first element of array, 
# arr[n-1] becomes second element, arr[0] becomes third element
# and so on.
# R2 = 0*arr[n-2] + 1*arr[n-1] +...+ (n-1)*arr[n-3]

# R2 - R1 = arr[0] + arr[1] + ... + arr[n-3] - (n-1)*arr[n-2] + arr[n-1]

# If we take a closer look at above values, we can observe 
# below pattern

# Rj - Rj-1 = arrSum - n * arr[n-j]

# Where arrSum is sum of all array elements, i.e., 

# arrSum = ∑ arr[i]
#         0<=i<=n-1 
# Below is complete algorithm: 

# 1) Compute sum of all array elements. Let this sum be 'arrSum'.

# 2) Compute R0 by doing i*arr[i] for given array. 
#    Let this value be currVal.

# 3) Initialize result: maxVal = currVal // maxVal is result.

# // This loop computes Rj from  Rj-1 
# 4) Do following for j = 1 to n-1
# ......a) currVal = currVal + arrSum-n*arr[n-j];
# ......b) If (currVal > maxVal)
#             maxVal = currVal   

# 5) Return maxVal

# return max possible value of sum(i*arr[i])
def maxsum(arr):

    # stores sum of arr[i]
    arrsum=0

    # stores sum of i*arr[i]
    currval=0

    n=len(arr)
    
    for i in range(0,n):
        arrsum= arrsum +arr[i]
        currval = currval +(i*arr[i])

    # initialize result
    maxval = currval

    # try all rotation one by one and find the maximum
    # rotation
    for j in range(1,n):
        currval = currval +arrsum-n*arr[n-j]
        if(currval > maxval):
            maxval = currval
        
    return maxval

arr =[10,1,2,3,4,5,6,7,8,9]
print("max sum is ",maxsum(arr))

# time complexity:O(n)
# auxiliary space:O(1)