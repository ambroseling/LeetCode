# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            else:
                max_left = max(node.left) + 1 
                max_right = max(node.right) + 1
                if max_left > max_right:
                    return max_left
                else:
                    return max_right
        return max(root)