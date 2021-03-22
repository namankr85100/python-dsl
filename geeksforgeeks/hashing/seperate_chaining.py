""" 
What is Collision?
Since a hash function gets us a small number for a key which is a big integer or string, there is a possibility that two keys result in the same value. The situation where a newly inserted key maps to an already occupied slot in the hash table is called collision and must be handled using some collision handling technique.




What are the chances of collisions with large table?
Collisions are very likely even if we have big table to store keys. An important observation is Birthday Paradox. With only 23 persons, the probability that two people have the same birthday is 50%.



How to handle Collisions?
There are mainly two methods to handle collision:
1) Separate Chaining
2) Open Addressing
In this article, only separate chaining is discussed. We will be discussing Open addressing in the next post.



Separate Chaining:
The idea is to make each cell of hash table point to a linked list of records that have same hash function value.




Let us consider a simple hash function as “key mod 7” and sequence of keys as 50, 700, 76, 85, 92, 73, 101.
hashChaining

C++ program for hashing with chaining

Advantages:
1) Simple to implement.
2) Hash table never fills up, we can always add more elements to the chain.
3) Less sensitive to the hash function or load factors.
4) It is mostly used when it is unknown how many and how frequently keys may be inserted or deleted.

Disadvantages:
1) Cache performance of chaining is not good as keys are stored using a linked list. Open addressing provides better cache performance as everything is stored in the same table.
2) Wastage of Space (Some Parts of hash table are never used)
3) If the chain becomes long, then search time can become O(n) in the worst case.
4) Uses extra space for links.



Performance of Chaining:
Performance of hashing can be evaluated under the assumption that each key is equally likely to be hashed to any slot of table (simple uniform hashing).

 m = Number of slots in hash table
 n = Number of keys to be inserted in hash table
 
 Load factor α = n/m 
  
 Expected time to search = O(1 + α)
 
 Expected time to delete = O(1 + α)

Time to insert = O(1)

 Time complexity of search insert and delete is 
 O(1) if  α is O(1)


Next Post:
Open Addressing for Collision Handling



References:
http://courses.csail.mit.edu/6.006/fall09/lecture_notes/lecture05.pdf

Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above

Attention reader! Don’t stop learning now. Get hold of all the important DSA concepts with the DSA Self Paced Course at a student-friendly price and become industry ready."""\
