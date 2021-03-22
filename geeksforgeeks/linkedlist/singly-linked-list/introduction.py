# Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers.
# linkedlist

# Why Linked List?
# Arrays can be used to store linear data of similar types, but arrays have the following limitations.
# 1) The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.
# 2) Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted.

# For example, in a system, if we maintain a sorted list of IDs in an array id[].

# id[] = [1000, 1010, 1050, 2000, 2040].




# And if we want to insert a new ID 1005, then to maintain the sorted order, we have to move all the elements after 1000 (excluding 1000).
# Deletion is also expensive with arrays until unless some special techniques are used. For example, to delete 1010 in id[], everything after 1010 has to be moved.

# Advantages over arrays
# 1) Dynamic size
# 2) Ease of insertion/deletion

# Drawbacks:
# 1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation. Read about it here.
# 2) Extra memory space for a pointer is required with each element of the list.
# 3) Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.

# Representation:
# A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL.
# Each node in a list consists of at least two parts:
# 1) data
# 2) Pointer (Or Reference) to the next node
# In C, we can represent a node using structures. Below is an example of a linked list node with integer data.
# In Java or C#, LinkedList can be represented as a class and a Node as a separate class. The LinkedList class contains a reference of Node class type.

# class Node:

#     #function to initialize the node object
#     def __init__(self,data):
#         self.data = data #assign data
#         self.read = None #initialize  next as null

# class LinkdeList:
#     #function to initialize the Linked List object
#     def __init__(self):
#         self.head - None

# let us create  a simple linkedlist with 3 nodes
# class Node:

#     def __init__(self,data):
#         self.data  = data #assign data
#         self.next = None #initialize next as null

# #linked List class contains a node object
# class LinkedList:
#     #function to initialize head
#     def __init__(self):
#         self.head = None

# #code execution starts here
# if __name__ == '__main__':
#     #start with the empty list
#     llist = LinkedList()
#     llist.head = Node(1)
#     second = Node(2)
#     third = Node(3)

    # ''' 
    # Three nodes have been created. 
    # We have references to these three blocks as head, 
    # second and third 
  
    # llist.head        second              third 
    #      |                |                  | 
    #      |                |                  | 
    # +----+------+     +----+------+     +----+------+ 
    # | 1  | None |     | 2  | None |     |  3 | None | 
    # +----+------+     +----+------+     +----+------+ 
    # '''

    # llist.head.next = second #use first node with second

    #  ''' 
    # Now next of first Node refers to second.  So they 
    # both are linked. 
  
    # llist.head        second              third 
    #      |                |                  | 
    #      |                |                  | 
    # +----+------+     +----+------+     +----+------+ 
    # | 1  |  o-------->| 2  | null |     |  3 | null | 
    # +----+------+     +----+------+     +----+------+  
    # '''

    # second.next = third #link second node with the third node

    #   ''' 
    # Now next of second Node refers to third.  So all three 
    # nodes are linked. 
  
    # llist.head        second              third 
    #      |                |                  | 
    #      |                |                  | 
    # +----+------+     +----+------+     +----+------+ 
    # | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    # +----+------+     +----+------+     +----+------+  


# Linked List Traversal
    # In the previous program, we have created a simple linked list with three nodes.
    # Let us traverse the created list and print the data of each node. 
    # For traversal, let us write a general-purpose function printList() that prints any given list.


class Node:
    #function to initialize the node object
    def __init__(self,data):
        self.data = data #assign data
        self.next = None #initialize next as well

#linked list class contains a node object
class LinkedList:
    #function to initialize head
    def __init__(self):
        self.head= None
    
    #this function prints contents of Linkde List
    #starting from head
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next

#cdde execution starts here
if __name__=='__main__':
    #start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(1)

    llist.head.next = second #link first node with second
    second.next = third

    llist.printlist( )
