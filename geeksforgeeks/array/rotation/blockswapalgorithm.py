# recursive implementaion
# it left rotates arr by d
def leftrotate(arr,d,n):
    leftrotaterec(arr,0,d,n)

def leftrotaterec(arr,i,d,n):

    # return if number of elements to be rotated
    # is zero or equal to array size
    if(d==0 or d==n):
        return

    # if number of elements to be rotated
    # is exactly half of array size
    if(n-d == d):
        swap(arr,i,n-d+i,d)
        leftrotaterec(arr,i,d,n-d)
        return

    #if a is shorter
    if(d < n - d):
        swap(arr,i,n-d+i,d)
        leftrotaterec(arr,i,d,n-d)
    else:
        swap(arr,i,d,n-d)
        
        # this is tricky
        leftrotaterec(arr,n-d+i,2*d-n,d)


def swap(arr,fi,si,d):
    for i in range(d):
        temp = arr[fi+i]
        arr[fi+i]=arr[si+i]
        arr[si+i]=temp     

def printarray(arr,size):
    for i in range(size):
        print(arr[i],end=" ")
    print()

if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7]
    leftrotate(arr,2,7)
    printarray(arr,7) 

# second method
# iterative implementaion
def leftrotate(arr, d, n): 
	if(d == 0 or d == n): 
		return; 
	i = d 
	j = n - d 
	while (i != j): 
		
		if(i < j): # A is shorter
			swap(arr, d - i, d + j - i, i) 
			j -= i 
		
		else: # B is shorter
			swap(arr, d - i, d, j) 
			i -= j 
	
	swap(arr, d - i, d, i)
#time complexity : O(n)


    

if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7]
    leftrotate(arr,2,7)
    printarray(arr,7)
