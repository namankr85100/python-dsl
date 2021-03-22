# Given a singly linked list and a position, delete a linked list node at the given position.

# Example:  

# Input: position = 1, Linked List = 8->2->3->1->7
# Output: Linked List =  8->3->1->7

# Input: position = 0, Linked List = 8->2->3->1->7
# Output: Linked List = 2->3->1->7


 
# If the node to be deleted is the root, simply delete it. To delete a middle node, we must have a pointer to the node previous to the node to be deleted. So if positions are not zero, we run a loop position-1 times and get a pointer to the previous node.

# Below is the implementation of the above idea.

class Node:

    #constructor to initialize the node object
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    #constructor to initialize head
    def __init__(self):
        self.head = None
    
    #function to inset a new node at the beginning
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    #given a reference to the head of a list
    #and a postion ,delete the node at a given postion
    def deletenode(self,position):

        #if linkedlist is empty
        if self.head == None:
            return
        
        #store head node
        temp = self.head

        #if head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        #find previous node of the node to be deleted
        for i in range(position-1):
            temp = temp.next
            if temp is not None:
                break

        
        #if position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return
        
        #node temp.next is the node to be deleted
        #store pointer to the next of node to be deleted
        next = temp.next.next

        #unlink the node from linke list
        temp.next = None

        temp.next = next
    
    #utility function to print the linked linkedlist
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp= temp.next

#driver program to test above function
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)

print("created linked list")
llist.printlist()
llist.deletenode(4)
print("unlinked list after deletion at position 4")
llist.printlist()
