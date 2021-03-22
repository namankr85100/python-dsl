# The problem is opposite of this post. We are given a Queue data structure that supports standard operations like enqueue() and dequeue(). We need to implement a Stack data structure using only instances of Queue and Queue operations allowed on the instances.

# A stack can be implemented using two queues. Let stack to be implemented be ‘s’ and queues used to implement be ‘q1’ and ‘q2’. Stack ‘s’ can be implemented in two ways:

# Method 1 (By making push operation costly)
# This method makes sure that newly entered element is always at the front of ‘q1’, so that pop operation just dequeues from ‘q1’. ‘q2’ is used to put every new element at front of ‘q1’.

# push(s, x) operation’s step are described below:
# Enqueue x to q2
# One by one dequeue everything from q1 and enqueue to q2.
# Swap the names of q1 and q2
# pop(s) operation’s function are described below:
# Dequeue an item from q1 and return it.


# Program to implement a stack using 
# two queue 
from queue import Queue 

class Stack: 
	
	def __init__(self): 
		
		# Two inbuilt queues 
		self.q1 = Queue() 
		self.q2 = Queue() 
			
		# To maintain current number 
		# of elements 
		self.curr_size = 0

	def push(self, x): 
		self.curr_size += 1

		# Push x first in empty q2 
		self.q2.put(x) 

		# Push all the remaining 
		# elements in q1 to q2. 
		while (not self.q1.empty()): 
			self.q2.put(self.q1.queue[0]) 
			self.q1.get() 

		# swap the names of two queues 
		self.q = self.q1 
		self.q1 = self.q2 
		self.q2 = self.q 

	def pop(self): 

		# if no elements are there in q1 
		if (self.q1.empty()): 
			return
		self.q1.get() 
		self.curr_size -= 1

	def top(self): 
		if (self.q1.empty()): 
			return -1
		return self.q1.queue[0] 

	def size(self): 
		return self.curr_size 

# Driver Code 
if __name__ == '__main__': 
	s = Stack() 
	s.push(1) 
	s.push(2) 
	s.push(3) 

	print("current size: ", s.size()) 
	print(s.top()) 
	s.pop() 
	print(s.top()) 
	s.pop() 
	print(s.top()) 

	print("current size: ", s.size())


# Method 2 (By making pop operation costly)
# In push operation, the new element is always enqueued to q1. In pop() operation, if q2 is empty then all the elements except the last, are moved to q2. Finally the last element is dequeued from q1 and returned.

# push(s, x) operation:
# Enqueue x to q1 (assuming size of q1 is unlimited).
# pop(s) operation:
# One by one dequeue everything except the last element from q1 and enqueue to q2.
# Dequeue the last item of q1, the dequeued item is result, store it.
# Swap the names of q1 and q2
# Return the item stored in step 2

# /* Java Program to implement a stack 
# using two queue */
# import java.util.*; 

# class Stack { 
# 	Queue<Integer> q1 = new LinkedList<>(), q2 = new LinkedList<>(); 
# 	int curr_size; 

# 	public Stack() 
# 	{ 
# 		curr_size = 0; 
# 	} 

# 	void remove() 
# 	{ 
# 		if (q1.isEmpty()) 
# 			return; 

# 		// Leave one element in q1 and 
# 		// push others in q2. 
# 		while (q1.size() != 1) { 
# 			q2.add(q1.peek()); 
# 			q1.remove(); 
# 		} 

# 		// Pop the only left element 
# 		// from q1 
# 		q1.remove(); 
# 		curr_size--; 

# 		// swap the names of two queues 
# 		Queue<Integer> q = q1; 
# 		q1 = q2; 
# 		q2 = q; 
# 	} 

# 	void add(int x) 
# 	{ 
# 		q1.add(x); 
# 		curr_size++; 
# 	} 

# 	int top() 
# 	{ 
# 		if (q1.isEmpty()) 
# 			return -1; 

# 		while (q1.size() != 1) { 
# 			q2.add(q1.peek()); 
# 			q1.remove(); 
# 		} 

# 		// last pushed element 
# 		int temp = q1.peek(); 

# 		// to empty the auxiliary queue after 
# 		// last operation 
# 		q1.remove(); 

# 		// push last element to q2 
# 		q2.add(temp); 

# 		// swap the two queues names 
# 		Queue<Integer> q = q1; 
# 		q1 = q2; 
# 		q2 = q; 
# 		return temp; 
# 	} 

# 	int size() 
# 	{ 
# 		return curr_size; 
# 	} 

# 	// Driver code 
# 	public static void main(String[] args) 
# 	{ 
# 		Stack s = new Stack(); 
# 		s.add(1); 
# 		s.add(2); 
# 		s.add(3); 
# 		s.add(4); 

# 		System.out.println("current size: " + s.size()); 
# 		System.out.println(s.top()); 
# 		s.remove(); 
# 		System.out.println(s.top()); 
# 		s.remove(); 
# 		System.out.println(s.top()); 
# 		System.out.println("current size: " + s.size()); 
# 	} 
# } 

