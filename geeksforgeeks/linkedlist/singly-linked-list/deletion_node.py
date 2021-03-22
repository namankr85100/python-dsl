# Let us formulate the problem statement to understand the deletion process. Given a ‘key’, delete the first occurrence of this key in the linked list. 

# Iterative Method:
# To delete a node from the linked list, we need to do the following steps. 
# 1) Find the previous node of the node to be deleted. 
# 2) Change the next of the previous node. 
# 3) Free memory for the node to be deleted.Let us formulate the problem statement to understand the deletion process. Given a ‘key’, delete the first occurrence of this key in the linked list. 

# Iterative Method:
# To delete a node from the linked list, we need to do the following steps. 
# 1) Find the previous node of the node to be deleted. 
# 2) Change the next of the previous node. 
# 3) Free memory for the node to be deleted.

#node class
class Node:
    #constructor to initialize the node object
    def __init__(self,data):
        self.data = data
        self.next= None

class LinkedList:

    #function to initialize head
    def __init__(self):
        self.head = None

    #function to insert a new node at the beginning
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    #given a reference to the head of a list and a key
    #delete the first occurence of ke in linkedlist
    def deletenode(self,key):
        #store head node
        temp = self.head

        #if head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        #search for the key to be deletef ,keep track of the
        # previous node as we need to change 'prev.next    
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        #if key was not present in linkedlist
        if temp == None:
            return

        #unlink the node from linked list
        prev.next = temp.next

        temp = None

    #utility function to print the linked linkedlist
    def printlist(self):
        temp  = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next

#driver program
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print("created Linked List:")
llist.printlist()
llist.deletenode(1)
print("linked list after deletion of 1")
llist.printlist()

