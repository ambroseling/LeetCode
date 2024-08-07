# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        def traversal(root,level):
            if root:
                if len(queue) == level:
                    queue.append(root.val)
                traversal(root.right,level+1)
                traversal(root.left,level+1)
        level = 0
        traversal(root,level)
        return queue
