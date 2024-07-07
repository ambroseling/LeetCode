# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# hard
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        intuition:
        we have 2 sums to worry about
        1) sum if current node's both children are part of path (with split)
        2) only 1 of current nodes children are considered (no split)
        '''
        if not root:
            return 0
        self.res = root.val # right now, our max is the root node
        def dfs(root):
            if not root:
                return 0
            # sum without splitting
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0) # if sum is negative, then dont add
            rightMax = max(rightMax, 0) # if sum is negative, then dont add

            # with splitting (consider both children):
            # we see if this path produces better result
            self.res = max(self.res, root.val+ leftMax + rightMax)
            
            return root.val + max(leftMax, rightMax) # we only want to consider the children 
        dfs(root)                                  # that is better return, + the node it self.
        return self.res
