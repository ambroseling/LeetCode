# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        paths = 0
        def pathSum(node):
            if node is None:
                return 0
            if node.val + pathSum(node.left) == targetSum:
                paths +=1
            elif node.val + pathSum(node.right) == targetSum:
                paths +=1
            return node.val
        x = pathSum(root)
        return paths