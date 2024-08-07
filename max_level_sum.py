


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sums = {}
        def traversal(node,level):
            if node:
                sums[level] = sums[level] + node.val if level in sums else node.val
                traversal(node.left,level+1)
                traversal(node.right,level+1)
        traversal(root,0)
        largest = list(sums.values())
        return largest.index(max(largest))+1

        