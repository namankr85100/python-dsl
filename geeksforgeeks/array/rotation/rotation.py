# ip:[1,2,3,4,5,6,7,8]
# d=2
# op:[3,4,5,6,7,8,1,2]

def leftrotate(arr,d,n):
    for i in range(d):
        leftrotatebyone(arr,n)

def leftrotatebyone(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i]= arr[i+1]
    arr[n-1] = temp

def printarr(arr,n):
    for i in range(n):
        print("%d "%arr[i],end="")    

arr = [1,2,3,4,5]
n = len(arr)
leftrotate(arr,2,n)
printarr(arr,n)       

# time complexity:O(n*d)
# auxiliary space :O(1)


# second approach
def leftrotate(arr,d,n):
    d= d % n
    g_c_d = gcd(d,n)
    for i in range(g_c_d):
        temp = arr[i]
        j=i
        while i:
            k  = j* d
            if k >= n:
                k = k-n
            if k == i:
                break
            arr[j] = arr[k]
            j=k
        arr[j]= temp

def printarray(arr,size):
    for i in range(size):
        print("%d"% arr[i],end="")

def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)


# time complexity :O(n)
# auxiliary space :O(1)

# main
arr  = [1,2,3,4,5,6,7]
n=len(arr)
d=2
leftrotate(arr,d,n)
printarray(arr,n)