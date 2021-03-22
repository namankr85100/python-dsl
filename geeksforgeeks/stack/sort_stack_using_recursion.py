# Given a stack, sort it using recursion. Use of any loop constructs like while, for..etc is not allowed. We can only use the following ADT functions on Stack S: 

# is_empty(S)  : Tests whether stack is empty or not.
# push(S)         : Adds new element to the stack.
# pop(S)         : Removes top element from the stack.
# top(S)         : Returns value of the top element. Note that this
#                function does not remove element from the stack.
# Example: 

# Input:  -3  <--- Top
#         14 
#         18 
#         -5 
#         30 

# Output: 30  <--- Top
#         18 
#         14 
#         -3 
#         -5 



"""
Algorithm 
We can use below algorithm to sort stack elements: 

sortStack(stack S)
    if stack is not empty:
        temp = pop(S);  
        sortStack(S); 
        sortedInsert(S, temp);
Below algorithm is to insert element is sorted order: 

sortedInsert(Stack S, element)
    if stack is empty OR element > top element
        push(S, elem)
    else
        temp = pop(S)
        sortedInsert(S, element)
        push(S, temp)
Illustration: 




Let given stack be
-3    <-- top of the stack
14
18
-5
30 
Let us illustrate sorting of stack using above example:
First pop all the elements from the stack and store poped element in variable ‘temp’. After poping all the elements function’s stack frame will look like:

temp = -3    --> stack frame #1
temp = 14    --> stack frame #2
temp = 18    --> stack frame #3
temp = -5    --> stack frame #4
temp = 30       --> stack frame #5
Now stack is empty and ‘insert_in_sorted_order()’ function is called and it inserts 30 (from stack frame #5) at the bottom of the stack. Now stack looks like below:

30    <-- top of the stack 
Now next element i.e. -5 (from stack frame #4) is picked. Since -5 < 30, -5 is inserted at the bottom of stack. Now stack becomes: 

30    <-- top of the stack
-5
Next 18 (from stack frame #3) is picked. Since 18 < 30, 18 is inserted below 30. Now stack becomes:

30    <-- top of the stack
18    
-5
Next 14 (from stack frame #2) is picked. Since 14 < 30 and 14 < 18, it is inserted below 18. Now stack becomes: 

30    <-- top of the stack
18
14    
-5
Now -3 (from stack frame #1) is picked, as -3 < 30 and -3 < 18 and -3 < 14, it is inserted below 14. Now stack becomes:

30    <-- top of the stack
18
14
-3    
-5
"""

# recursive method to inser element in sorted way
def sortedinsert(s,element):

    # base case:either stack is empty or newly inserted
    # item is greater than top (more than all existing)
    if len(s) == 0 or element >s[-1]:
        s.append(element)
        return
    else:
        #remove the top item and recur
        temp = s.pop()
        sortedinsert(s,element)

        #put back the top item removed earlier
        s.append(temp)

#method to sort stack

def sortstack(s):
    #if stack is not empty
    if len(s)!=0:
        #remove the top item
        temp = s.pop()

        #sort remaining stack
        sortstack(s)

        #push the top item in sorted stack
        sortedinsert(s,temp)

#printing contents of stack
def printstack(s):
    for i in s[::-1]:
        print(i,end=" ")
    print()

#driver code
if __name__=="__main__":
    s=[]
    s.append(30)
    s.append(-5)
    s.append(18)
    s.append(14)
    s.append(-3)
    print("stack elements before sorting:")
    printstack(s)

    sortstack(s)

    print("\n stack elements after sorting")
    printstack(s)

# Complexity Analysis: 

# Time Complexity: O(n2). 
# In the worst case for every sortstack(), sortedinsert() is called for ‘N’ times recursively for putting element to the right place
# Auxiliary Space: O(N)
# Use of stack data structure for storing values