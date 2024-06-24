class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        def pathSum(node, currSum):

            if node is None or currSum is None:
                return 0
            add = 0
            if currSum == targetSum:
                add +=1
            return max(pathSum(node.left,node.left.val if node.left else None) , pathSum(node.left,currSum+node.left.val if node.left else None)) + max( pathSum(node.right,node.right.val if node.right else None) , pathSum(node.right,currSum+node.right.val if node.right else None)) +add
        
        if root is not None:
            paths = pathSum(root,root.val)
            return paths
        else:
            return 0
