# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def goodNodes(node,greatest):
            if node is None:
                return 0
            if node.val >= greatest:
                return goodNodes(node.left, node.val) +  goodNodes(node.right,node.val) + 1
            else:
                return goodNodes(node.left,greatest) +  goodNodes(node.right,greatest)
        return goodNodes(root,root.val)