# Write a program to reverse a stack using recursion. You are not allowed to use loop constructs like while, for..etc, and you can only use the following ADT functions on Stack S: 
# isEmpty(S) 
# push(S) 
# pop(S)

# The idea of the solution is to hold all values in Function Call Stack until the stack becomes empty. When the stack becomes empty, insert all held items one by one at the bottom of the stack. 
# For example, let the input stack be  

#     1  <-- top
#     2
#     3
#     4    
# First 4 is inserted at the bottom.
#     4 <-- top

# Then 3 is inserted at the bottom
#     4 <-- top    
#     3

# Then 2 is inserted at the bottom
#     4 <-- top    
#     3 
#     2
     
# Then 1 is inserted at the bottom
#     4 <-- top    
#     3 
#     2
#     1
# So we need a function that inserts at the bottom of a stack using the above given basic stack function.
# void insertAtBottom((): First pops all stack items and stores the popped item in function call stack using recursion. And when stack becomes empty, pushes new item and all items stored in call stack.
# void reverse(): This function mainly uses insertAtBottom() to pop all items one by one and insert the popped items at the bottom.
"""
below is a recursion function
that inserts an element
at the bottom of a stack"""

def insertatbottom(stack,item):
    if isEmpty(stack):
        push(stack,item)
    else:
        temp = pop(stack)
        insertatbottom(stack,item)
        push(stack,temp)
"""
below is the function that reverses the given stack 
using insertatbottom""" 
def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertatbottom(stack,temp)
"""
below is a template running
program for testing above
function"""

"""
function to create a stack
it initializes size if stack
as 0"""
def createstack():
    stack=[]
    return stack
"""
function to check if
the stack is empty"""

def isEmpty(stack):
    return len(stack) == 0

"""
function to push an 
item to stack"""
def push(stack,item):
    stack.append(item)

# function to pop an element
def pop(stack):

    # if  stack is empty
    # then error
    if(isEmpty(stack)):
        print("stack underfloe")
        exit(1)
    return stack.pop()

# function to print the stack
def prints(stack):
    for i  in range(len(stack)-1,-1,-1):
        print(stack[i],end=' ')
    print()

#dricer code
stack = createstack()
push(stack,str(4))
push(stack,str(3))
push(stack,str(2))
push(stack,str(1))
print("original stack")
prints(stack)

reverse(stack)

print("reversed stack")
prints(stack)

# Time Complexity: This approach takes the worst time complexity of O(n^2), 

