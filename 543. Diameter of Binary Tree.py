# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def dfs(root):
            if not root:
                return -1
            l = dfs(root.left)
            r = dfs(root.right)
            res[0] = max(res[0], 2 + l + r)
            
            return 1 + max(l,r)
        dfs(root)
        return res[0]