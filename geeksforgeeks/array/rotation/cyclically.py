# input:arr[]={1,2,3,4,5}
# output:arr[]={5,1,2,3,4}

# following are steps
# 1.store last elements in a variable say x
# 2.shift all elements one position ahead
# 3.replace first element of array with x

# first method
def rotate(arr,n):
    x=arr[n-1]
    for i in range(n-1,0,-1):
        # print("\n this is original")
        # print(arr[i],end=" ")
        arr[i]=arr[i-1]
    arr[0]=x

#driver function
arr=[1,2,3,4,5]
n=len(arr)
print('given array is')
for i in range(0,n):
    print(arr[i],end=" ")
rotate(arr,n)
print("\n rotated array is")
for i in range(0,n):
    print(arr[i],end=" ")

# time complexity :O(n)
# auxiliary space :O(1)