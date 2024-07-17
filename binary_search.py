# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        import ipdb; ipdb.set_trace()
        def search(node):
            if node is None:
                return None
            if node.left and node.left.val == val:
                return node.left
            if node.right and node.right.val == val:
                return node.right
            if val < node.val:
                return search(node.left)
            if val > node.val:
                return search(node.right)
        
        if root.val == val:
            result =  root
        else:
            result = search(root)
            
        return result
        # def search(node):
        #     if node is None:
        #         return None
        #     if node.val == val:
        #         return node
        #     if val < node.val:
        #         return search(node.left)
        #     if val > node.val:
        #         return search(node.right)
        
        # result = search(root)
        # return result
if __name__ == "__main__":
    s = Solution()
    s.searchBST()