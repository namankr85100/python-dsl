# input :arr[] = [0,3,1,2]
# output:29
# explanation:lets look at all the rotations,
# {8,3,1,2} = 8*0+3*1+1*2+2*3=11
# {3,1,2,8} =3*0+1*1+2*2+8*3=29
# {1,2,8,2}=1*0+2*1+8*2+3*3=27
# {2,8,3,1}=2*0+8*1+3*2+1*3+1*3=17

# Input: arr[] = {3, 2, 1}
# Output: 7
# Explanation: Lets look at all the rotations,
# {3, 2, 1} = 3*0 + 2*1 + 1*2 = 4
# {2, 1, 3} = 2*0 + 1*1 + 3*2 = 7
# {1, 3, 2} = 1*0 + 3*1 + 2*2 = 7

# approach
# naive solution(n2)
# Approach:A simple solution is to try all possible rotations. Compute sum of i*arr[i] for every rotation and return maximum sum.
# Algorithm:
# Rotate the array for all values from 0 to n.
# Calculate the sum for each rotations.
# Check if the maximum sum is greater than the current sum then update the maximum sum.

import sys
def maxsum(arr,n):

    #initialize resule
    res = -sys.maxsize

    #consider the rotation beginning woth i
    #for all possible values of i
    for i in range(0,n):

        #initialize sum of current rotation
        curr_sum=0

        #compute sum of all values 
        #actually rotaion the array
        #compute sum by finding indexex when
        #arr[i] is first element
        for j in range(0,n):
            index = int((i+j)%n) #0+0/4=0  0+1/4=0 .. 0+4/4
            curr_sum+=j*arr[index]

        #update result if required
        res = max(res,curr_sum)
    return res

arr =[8,3,1,2]
n=len(arr)

print(maxsum(arr,n))
# time complexity :O(n2)

# second method
# Approach: The basic approach is to calculate the sum of new rotation from the previous rotations. This brings up a similarity where only the multipliers of first and last element change drastically and the multiplier of every other element increases or decreases by 1. So in this way, the sum of next rotation can be calculated from the sum of present rotation.
# Algorithm: 
# The idea is to compute the value of a rotation using values of previous rotation. When an array is rotated by one, following changes happen in sum of i*arr[i]. 
# Multiplier of arr[i-1] changes from 0 to n-1, i.e., arr[i-1] * (n-1) is added to current value.
# Multipliers of other terms is decremented by 1. i.e., (cum_sum – arr[i-1]) is subtracted from current value where cum_sum is sum of all numbers.


# next_val = curr_val - (cum_sum - arr[i-1]) + arr[i-1] * (n-1);

# next_val = Value of ∑i*arr[i] after one rotation.
# curr_val = Current value of ∑i*arr[i] 
# cum_sum = Sum of all array elements, i.e., ∑arr[i].

# Lets take example {1, 2, 3}. Current value is 1*0+2*1+3*2
# = 8. Shifting it by one will make it {2, 3, 1} and next value
# will be 8 - (6 - 1) + 1*2 = 5 which is same as 2*0 + 3*1 + 1*2
# An efficient Python3 program to
# compute maximum sum of i * arr[i]

def maxSum(arr, n):

	# Compute sum of all array elements
	cum_sum = 0
	
	for i in range(0, n):
		cum_sum += arr[i] 

	# Compute sum of i * arr[i] for 
	# initial configuration.
	curr_val = 0
	
	for i in range(0, n):
		curr_val += i * arr[i] 

	# Initialize result
	res = curr_val 

	# Compute values for other iterations
	for i in range(1, n):
	
		# Compute next value using previous
		# value in O(1) time
		next_val = (curr_val - (cum_sum - arr[i-1]) +
									arr[i-1] * (n-1))

		# Update current value
		curr_val = next_val 

		# Update result if required
		res = max(res, next_val)
	
	return res 


# Driver code
arr = [8, 3, 1, 2] 
n = len(arr)

print(maxSum(arr, n))
# time complexity :O(n)
# auxiliary space :O(1)

# method 3
# Method 3: The method discusses the solution using pivot in O(n) time. The pivot method can only be used in the case of a sorted or a rotated sorted array. For example: {1, 2, 3, 4} or {2, 3, 4, 1}, {3, 4, 1, 2} etc.

# Approach: Let’s assume the case of a sorted array. As we know for an array the maximum sum will be when the array is sorted in ascending order. In case of a sorted rotated array, we can rotate the array to make it in ascending order. So, in this case, the pivot element is needed to be found following which the maximum sum can be calculated.
# Algorithm: 
# Find the pivot of the array: if arr[i] > arr[(i+1)%n] then it is the pivot element. (i+1)%n is used to check for the last and first element.
# After getting pivot the sum can be calculated by finding the difference with the pivot which will be the multiplier and multiply it with the current element while calculating the sum

def maxsum(arr,n):
    sum=0
    pivot = findpivot(arr,n)

    #difference in pivot and index
    #of last element of array
    diff = n-1-pivot
    for i in range(n):
        sum = sum + ((i+diff)%n)*arr[i]
    return sum

#function to find pivot
def findpivot(arr,n):
    for i in range(n):
        if(arr[i]>arr[(i+1)%n]):
            return i

if __name__=="__main__":
    #rotated input array
    arr=[8,3,1,2]
    n=len(arr)
    max=maxsum(arr,n)
    print(max)

# Complexity analysis: 
# Time Complexity : O(n) 
# As only one loop was needed to traverse from 0 to n to find the pivot. To find the sum another loop was needed, so the complexity remains O(n).
# Auxiliary Space : O(1). 
# We do not require extra space to so the Auxiliary space is O(1)    


