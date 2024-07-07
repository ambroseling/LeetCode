# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# medium
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        """
        2 ways to do it, recursively, or iteratively
        I'll show both ways
        """
        # recursively:
        '''def in_order_traversal(root):
            
            if root is None:
                return [] 
            # here, if the root exists, we go to the left, which returns a list
            # then we add the current nodes value, by doing [#from left tree] + [root.val] 
            # which concatinates the two lists together
            # then we are traversing the right tree and seeing if values exist.   
            return in_order_traversal(root.left) + [root.val] + in_order_traversal(root.right)
        res = in_order_traversal(root)
        print(res)
        return res[k - 1]'''

        # iteratively:
        n = 0 # number of elements visited (in order), 
        # so when n==k, we have reached our solution
        stack = []
        cur = root
        # if stack is not empty, it means we still have nodes to process
        # if cur is not empty, it current node still needs to be processed
        while cur or stack:
            # we want to go left
            while cur: 
                stack.append(cur)
                cur = cur.left
            # we can no longer go left
            cur = stack.pop()
            n += 1
            if n == k: # we always have k nodes in the tree
                return cur.val
            cur = cur.right

# Follow up: If the BST is modified often (i.e., we can do insert 
# and delete operations) and you need to find the kth smallest frequently,
# how would you optimize?
# # 
# We add a new piece of information to each node called size, 
# which tells us how many nodes are in the subtree rooted at 
# that node (including the node itself).

# Steps:
# Insert a Node:

# When you insert a new value into the BST, you follow the usual BST insert procedure.
# Additionally, each time you insert a node, you update the size attribute for 
# each node you pass by on your way down the tree.

# Delete a Node:

# When you delete a value, you follow the usual BST delete procedure.
# Again, you update the size attribute for each node you pass by during the deletion process.
# Find the k-th Smallest Element:

# Use the size attribute to quickly find the k-th smallest element without traversing the entire tree.
# If you know the sizes of the left subtrees, you can decide whether to go left, return the current node, or go right.

