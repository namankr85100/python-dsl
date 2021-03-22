"""
Print a Binary Tree in Vertical Order | Set 2 (Map based Method)


Given a binary tree, print it vertically. The following example illustrates the vertical order traversal.

           1
        /    \ 
       2      3
      / \   /   \
     4   5  6   7
               /  \ 
              8   9 
               
              
The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9
 

print-binary-tree-in-vertical-order

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
We have discussed a O(n2) solution in the previous post. In this post, an efficient solution based on the hash map is discussed. We need to check the Horizontal Distances from the root for all nodes. If two nodes have the same Horizontal Distance (HD), then they are on the same vertical line. The idea of HD is simple. HD for root is 0, a right edge (edge connecting to right subtree) is considered as +1 horizontal distance and a left edge is considered as -1 horizontal distance. For example, in the above tree, HD for Node 4 is at -2, HD for Node 2 is -1, HD for 5 and 6 is 0 and HD for node 7 is +2. 
We can do preorder traversal of the given Binary Tree. While traversing the tree, we can recursively calculate HDs. We initially pass the horizontal distance as 0 for root. For left subtree, we pass the Horizontal Distance as Horizontal distance of root minus 1. For right subtree, we pass the Horizontal Distance as Horizontal Distance of root plus 1. For every HD value, we maintain a list of nodes in a hash map. Whenever we see a node in traversal, we go to the hash map entry and add the node to the hash map using HD as a key in a map.
Following is the C++ implementation of the above method. Thanks to Chirag for providing the below C++ implementation.
"""
# Python program for printing vertical order of a given
# binary tree

# A binary tree node
class Node:
	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Utility function to store vertical order in map 'm' 
# 'hd' is horizontal distance of current node from root
# 'hd' is initially passed as 0
def getVerticalOrder(root, hd, m):

	# Base Case
	if root is None:
		return
	
	# Store current node in map 'm'
	try:
		m[hd].append(root.key)
	except:
		m[hd] = [root.key]
	
	# Store nodes in left subtree
	getVerticalOrder(root.left, hd-1, m)
	
	# Store nodes in right subtree
	getVerticalOrder(root.right, hd+1, m)

# The main function to print vertical order of a binary
#tree ith given root
def printVerticalOrder(root):
	
	# Create a map and store vertical order in map using
	# function getVerticalORder()
	m = dict()
	hd = 0
	getVerticalOrder(root, hd, m)
	
	# Traverse the map and print nodes at every horizontal
	# distance (hd)
	for index, value in enumerate(sorted(m)):
		for i in m[value]:
			print (i,end= " ")
		print


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print ("Vertical order traversal is")
printVerticalOrder(root)


#Another Approach using computeIfAbsent method:

# We can write the code in a more concise way, by using computeIfAbsent method of the map in java and by using a treemap for natural sorting based upon keys.

# Below is the implementation of above approach.

"""
// Java Program for above approach
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

class Node {
	int data;
	Node left, right;

	Node(int item)
	{
		data = item;
		left = right = null;
	}
}

public class BinaryTree {

	Node root;

	// Values class
	class Values {
		int max, min;
	}

	// Program to find vertical Order
	public void verticalOrder(Node node)
	{
		Values val = new Values();

		// Create TreeMap
		Map<Integer, List<Integer> > map
			= new TreeMap<Integer, List<Integer> >();

		// Function Call to findHorizonatalDistance
		findHorizonatalDistance(node, val, val, 0, map);

		// Iterate over map.values()
		for (List<Integer> list : map.values()) {
			System.out.println(list);
		}

		// Print "done"
		System.out.println("done");
	}

	// Program to find Horizonatal Distance
	public void findHorizonatalDistance(
		Node node, Values min, Values max, int hd,
		Map<Integer, List<Integer> > map)
	{

		// If node is null
		if (node == null)
			return;

		// if hd is less than min.min
		if (hd < min.min)
			min.min = hd;

		// if hd is greater than min.min
		if (hd > max.max)
			max.max = hd;

		// Using computeIfAbsent
		map.computeIfAbsent(hd,
							k -> new ArrayList<Integer>())
			.add(node.data);

		// Function Call with hd equal to hd - 1
		findHorizonatalDistance(node.left, min, max, hd - 1,
								map);

		// Function Call with hd equal to hd + 1
		findHorizonatalDistance(node.right, min, max,
								hd + 1, map);
	}

	// Driver Code
	public static void main(String[] args)
	{

		BinaryTree tree = new BinaryTree();

		/* Let us construct the tree shown
							in above diagram */
		tree.root = new Node(1);
		tree.root.left = new Node(2);
		tree.root.right = new Node(3);
		tree.root.left.left = new Node(4);
		tree.root.left.right = new Node(5);
		tree.root.right.left = new Node(6);
		tree.root.right.right = new Node(7);
		tree.root.right.left.right = new Node(8);
		tree.root.right.right.right = new Node(9);

		System.out.println("vertical order traversal is :");

		// Function Call
		tree.verticalOrder(tree.root);
	}
}
"""
