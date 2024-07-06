# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# medium
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Intuition:
        We start off on the root node, and start traversing down recursively, hence why we are using 
        dfs.
        Now our dfs gets passed in the node, and the current maxValue it has seen down its path
        This allows us to compare, whether or not our node is a good node, or not.
        Then, we simply add 1 to the result if it is, and 0 if its not.
        Update the maxVal, considering the node we just saw
        We then recursively pass the dfs to the children, left and right.
        Then, we simply return the res of dfs(root, root.val) as it returns the total nodes we have seen.
        """
        
        def dfs (node, maxVal):
            if not node:
                return 0
            
            result = 1 if (node.val >= maxVal) else 0
            maxVal = max(node.val, maxVal)
            result += dfs(node.left, maxVal)
            result += dfs(node.right, maxVal)
            return result    
        return dfs(root,root.val)
