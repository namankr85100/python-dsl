# Like Stack, Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO).  A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.
# The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.

# Operations on Queue:
# Mainly the following four basic operations are performed on queue:

# Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
# Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition.
# Front: Get the front item from queue.
# Rear: Get the last item from queue.

# queue

# Applications of Queue:
# Queue is used when things don’t have to be processed immediatly, but have to be processed in First InFirst Out order like Breadth First Search. This property of Queue makes it also useful in following kind of scenarios.




# 1) When a resource is shared among multiple consumers. Examples include CPU scheduling, Disk Scheduling.
# 2) When data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes. Examples include IO Buffers, pipes, file IO, etc.

# See this for more detailed applications of Queue and Stack.

# Array implementation Of Queue
# For implementing queue, we need to keep track of two indices, front and rear. We enqueue an item at the rear and dequeue an item from the front. If we simply increment front and rear indices, then there may be problems, the front may reach the end of the array. The solution to this problem is to increase front and rear in circular manner (See this for details)


# class queue to represent a queue
class Queue:
    #__init__function
    def __init__(self,capacity):
        self.front = self.size =0
        self.rear = capacity -1
        self.q = [None]*capacity
        self.capacity = capacity
    
    #queue is full when size becomes
    #equal to the capacity
    def isfull(self):
        return self.size == self.capacity
    
    #queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    #function to add an item to the queue
    #it changes rear and size
    def enqueue(self,item):
        if self.isfull():
            print("full")
            return
        self.rear =(self.rear +1)%(self.capacity)
        self.q[self.rear] = item
        self.size = self.size +1
        print("s enqueued to queue",str(item))

    #function to remove an item from queue
    #it changes front and size
    def dequeue(self):
        if self.isEmpty():
            print("empty")
            return
        
        print("dequeued from queue",str(self.q[self.front]))
        self.front = (self.front +1)%(self.capacity)
        self.size = self.size -1

    #function to get front of queue
    def que_front(self):
        if self.isEmpty():
            print("queue is mepty")

        print("front item is",self.q[self.front])

    #function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print("queue is empty")
        print("rear item is ",self.q[self.rear])

#driver code
if __name__=="__main__":
    queue = Queue(30)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.dequeue()
    queue.que_front()
    queue.que_rear()


# Complexity Analysis:     



""" Applications of Queue Data Structure
Queue is used when things don’t have to be processed immediately, but have to be processed in First In First Out order like Breadth First Search. This property of Queue makes it also useful in following kind of scenarios.
1) When a resource is shared among multiple consumers. Examples include CPU scheduling, Disk Scheduling.
2) When data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes. Examples include IO Buffers, pipes, file IO, etc.

See this for more detailed applications of Queue and Stack.

References:
http://introcs.cs.princeton.edu/43stack/
Attention reader! Don’t stop learning now. Get hold of all the important DSA concepts with the DSA Self Paced Course at a student-friendly price and become industry ready."""