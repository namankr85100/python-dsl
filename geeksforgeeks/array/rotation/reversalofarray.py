# rotate(arr[],d,n)
# reverse(arr[],1,d):
# reverse(arr[],d+1,n):
# reverse(arr[],1,n)


# arr[]=[1,2,3,4,5,6,7]
# d=2
# n=7
# A=[1,2] and B=[3,4,5,6,7]

# reverse A , we get ArB =[2,1,3,4,5,6,7]
# reverse B, we get ArBr = [2,1,7,6,5,4,3]
# reverse all the arr (ArBr) = [3,4,5,6,7,1,2]


# method 1
def leftrotate(arr,d):
    if d==0:
        return
    n = len(arr)
    # in this case rotating factor is greator 
    #than array length
    d = d % n
    reversarray(arr,0,d-1)
    reversarray(arr,d,n-1)
    reversarray(arr,0,n-1)

def reversarray(arr,start,end):
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start +=1
        end =end-1

def printarray(arr):            
    for  i in range(0,len(arr)):
        print("%d "%arr[i],end="") 

# time complexity :O(n)


#main
arr = [1,2,3,4,5,6,7]
n = len(arr)
d = 2
leftrotate(arr,d) #roatate array by 2
printarray(arr)