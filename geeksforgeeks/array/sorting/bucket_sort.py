# Bucket sort is mainly useful when input is uniformly distributed over a range. For example, consider the following problem. 
# Sort a large set of floating point numbers which are in range from 0.0 to 1.0 and are uniformly distributed across the range. How do we sort the numbers efficiently?
# A simple way is to apply a comparison based sorting algorithm. The lower bound for Comparison based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is Ω(n Log n), i.e., they cannot do better than nLogn. 
# Can we sort the array in linear time? Counting sort can not be applied here as we use keys as index in counting sort. Here keys are floating point numbers.  
# The idea is to use bucket sort. Following is bucket algorithm.

# bucketSort(arr[], n)
# 1) Create n empty buckets (Or lists).
# 2) Do following for every array element arr[i].
# .......a) Insert arr[i] into bucket[n*array[i]]
# 3) Sort individual buckets using insertion sort.
# 4) Concatenate all sorted buckets.

# Time Complexity: If we assume that insertion in a bucket takes O(1) time then steps 1 and 2 of the above algorithm clearly take O(n) time. The O(1) is easily possible if we use a linked list to represent a bucket (In the following code, C++ vector is used for simplicity). Step 4 also takes O(n) time as there will be n items in all buckets. 
# The main step to analyze is step 3. This step also takes O(n) time on average if all numbers are uniformly distributed (please refer CLRS book for more details)
# Following is the implementation of the above algorithm.


def insertionsort(b):
    for i in range(1,len(b)):
        up=b[i]
        j=i-1
        while j>=0 and b[j]>up:
            b[j+1]=b[j]
            j-=1
        b[j+1]=up
    return b

def bucketsort(x):
    arr=[]
    slot_num=10 #10 means 10 slots,each slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

    #put array elements in different buckets
    for j in x:
        index_b=int(slot_num*j)
        arr[index_b].append(j)

    #sort individual buckets
    for i in range(slot_num):
        arr[i]=insertionsort(arr[i])

    #concatenate the result
    k=0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k+=1
    return x

# driver code
x=[0.897,0.565,0.656,0.1234,0.665,0.3434]
print('sorted array is')
print(bucketsort(x))


# Bucket Sort for numbers having integer part:
# Algorithm : 

# Find maximum element and minimum of the array
# Calculate the range of each bucket
#           range = (max - min) / n
#           n is the number of buckets
#         3. Create n buckets of calculated range

#         4. Scatter the array elements to these buckets

#           BucketIndex = ( arr[i] - min ) / range
#         6. Now sort each bucket individually

#         7. Gather the sorted elements from buckets to original array

# Input :    
# Unsorted array:  [ 9.8 , 0.6 , 10.1 , 1.9 , 3.07 , 3.04 , 5.0 , 8.0 , 4.8 , 7.68 ]
# No of buckets :  5

# Output :  
# Sorted array:   [ 0.6 , 1.9 , 3.04 , 3.07 , 4.8 , 5.0 , 7.68 , 8.0 , 9.8 , 10.1 ]
