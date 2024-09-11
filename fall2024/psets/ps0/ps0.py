#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # Your code goes here
    #Base Case for if the node is none
    if v == None:
        return 0
    #calculate size of left tree
    left_size = calculate_sizes(v.left)
    #calculate size of right tree
    right_size = calculate_sizes(v.right)

    #total size of subtree
    v.size = left_size + right_size + 1

    return v.size

#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):
    # Your code goes here 
    #question: do we already know that the inputed v has size at greater than or equal to 2t+1
    #Base Case for if the node is none
    if v == None:
        return None
    
    #check if the vertex we're looking for the current vertex v
    #question: do we use v or calculate_sizes(v)
    if t <= v.size <= 2*t: #if the size is between t and 2t inclusive then we have found vertex v
        return v
    
    #check if the key in the left tree, if yes then return true
    #if left child exists, check if its subtree has size between t and 2t, if not keep going down the left branch
    if v.left !=None and v.left.size >=t: 
        w = FindDescendantOfSize(t, v.left)
        return w
    
    #if right child exists, check that and go down right branch
    if v.right !=None and v.right.size >=t:
        w = FindDescendantOfSize(t, v.right)
        return w
    
    return None #if such a vertex does not exist in tree