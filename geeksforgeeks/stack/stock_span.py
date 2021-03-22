# The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate span of stock’s price for all n days.
# The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
# For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}

# A Simple but inefficient method
# Traverse the input price array. For every element being visited, traverse elements on left of it and increment the span value of it while elements on the left side are smaller.

# Following is implementation of this method.

#fills list s[] with span values
def calculatespan(price,n,s):


    #span value of first day is always 1
    s[0]=1

    #calculate span value of remaining days by linearly
    #checking previous days
    for i in range(1,n,1):
        s[i] = 1 #initialie span value

        #traverse left while the next element on left is
        #smaller than price[i]
        j=i-1
        while(j>=0 and price[i]>=price[j]):
            s[i] +=1
            j -= 1

#a utility function to print elements of array
def printarray(arr,n):
    for i in range(n):
        print(arr[i],end = " ")

#driver program to test above function
price=[10,4,5,90,120,80]
n=len(price)
s=[None]*n

#fill the span values in list s[]
calculatespan(price ,n,s)

#print the calculated span values
printarray(s,n)




print()

# second method
# Python linear time solution for stock span problem 

# A stack based efficient method to calculate s 
def calculateSpan(price, S): 
	
	n = len(price) 
	# Create a stack and push index of fist element to it 
	st = [] 
	st.append(0) 

	# Span value of first element is always 1 
	S[0] = 1

	# Calculate span values for rest of the elements 
	for i in range(1, n): 
		
		# Pop elements from stack whlie stack is not 
		# empty and top of stack is smaller than price[i] 
		while( len(st) > 0 and price[st[-1]] <= price[i]): 
			st.pop() 

		# If stack becomes empty, then price[i] is greater 
		# than all elements on left of it, i.e. price[0], 
		# price[1], ..price[i-1]. Else the price[i] is 
		# greater than elements after top of stack 
		S[i] = i + 1 if len(st) <= 0 else (i - st[-1]) 

		# Push this element to stack 
		st.append(i) 


# A utility function to print elements of array 
def printArray(arr, n): 
	for i in range(0, n): 
		print (arr[i], end =" ") 


# Driver program to test above function 
price = [10, 4, 5, 90, 120, 80] 
S = [0 for i in range(len(price)+1)] 

# Fill the span values in array S[] 
calculateSpan(price, S) 

# Print the calculated span values 
printArray(S, len(price)) 




# Time Complexity: O(n). It seems more than O(n) at first look. If we take a closer look, we can observe that every element of the array is added and removed from the stack at most once. So there are total 2n operations at most. Assuming that a stack operation takes O(1) time, we can say that the time complexity is O(n).

# Auxiliary Space: O(n) in worst case when all elements are sorted in decreasing order.

# Another approach: (without using stack)




print()
#third method

""" an efficient method to calculate
stock span values implementing
the time idea wihtout using stack """
# Python3 program for a linear time 
# solution for stock span problem 
# without using stack 

# An efficient method to calculate 
# stock span values implementing 
# the same idea without using stack 
def calculateSpan(A, n, ans): 
	
	# Span value of first element 
	# is always 1 
	ans[0] = 1

	# Calculate span values for rest 
	# of the elements 
	for i in range(1, n): 
		counter = 1
		
		while ((i - counter) >= 0 and
			A[i] >= A[i - counter]): 
			counter += ans[i - counter] 
		ans[i] = counter 

# A utility function to print elements 
# of array 
def printArray(arr, n): 
	
	for i in range(n): 
		print(arr[i], end = ' ') 
	print() 

# Driver code 
price = [ 10, 4, 5, 90, 120, 80 ] 
n = len(price) 
S = [0] * (n) 

# Fill the span values in array S[] 
calculateSpan(price, n, S) 

# Print the calculated span values 
printArray(S, n) 
