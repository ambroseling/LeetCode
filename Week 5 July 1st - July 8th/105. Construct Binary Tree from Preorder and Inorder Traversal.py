# Definition for a binary tree node.
# medium

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        """
        Intuition:
        we are going to cross reference both lists, and deduce from that,
        1) starting root node (always first node in preorder)
        2) where to divide into sublists AKA mid point
        3) recursively call each subsection, as the properties 1) and 2) still hold true
        """
        if not preorder or not inorder:
            return None
        # from 1)
        root = TreeNode(preorder[0])
        # from 2) 
        mid = inorder.index(preorder[0])
        # 3)
        root.left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root