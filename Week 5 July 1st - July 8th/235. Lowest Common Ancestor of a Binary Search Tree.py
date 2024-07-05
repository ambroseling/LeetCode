# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Medium
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # because its binary search tree, all values lower are on the left, and bigger on right.
        # therefore, we can just return the node which falls right in between both p and q, inclusive
        # as we are going top down
        if root.val > max(p.val,q.val):
            return self.lowestCommonAncestor(root.left, p,q)
        elif root.val < min(p.val,q.val):
            return self.lowestCommonAncestor(root.right, p,q)
        return root

