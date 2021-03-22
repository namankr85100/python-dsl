# exmaple:
# Input : arr[] = {12, 10, 5, 6, 52, 36}
#             k = 2
# Output : arr[] = {5, 6, 52, 36, 12, 10}
# Explanation : Split from index 2 and first 
# part {12, 10} add to the end .

# Input : arr[] = {3, 1, 2}
#            k = 1
# Output : arr[] = {1, 2, 3}
# Explanation : Split from index 1 and first
# part add to the end.

# simple solution : rotate array one by one

def splitarr(arr,n,k):
    for i in range(0,k):
        x = arr[0]
        for j in range(0,n-1):
            arr[j] = arr[j+1]

        arr[n-1]=x

#main
arr=[12,10,5,6,52,36]
n=len(arr)
position = 3

splitarr(arr,n,position)
for i in range(0,n):
    print(arr[i],end= " ")

# time complexity:O(nk)

# Method second:
# Another approach: An another approach is to make a temporary array with double the size and copy our array element in to new array twice .and then copy element from new array to our array by taking the rotation as starting index upto the length of our array.

# Below is the implementation of above approach.

def splitandadd(a,length,rotation):

    #make a temporary array with double
    #the size and each index is initialized to a 
    tmp=[0 for i in range(length*2)]

    #copy array element to new array twice
    for i in range(length):
        tmp[i]=a[i]
        tmp[i+length]=a[i]

    for i in range(rotation,rotation +length,1):
        a[i-rotation]=tmp[i]

#driver code
print()
arr=[12,10,5,6,52,36]
n=len(arr)
position=2
splitandadd(arr,n,position)
for i in range(n):
    print(arr[i],end=" ")
print()
