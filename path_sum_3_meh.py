class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        visited = []
        def pathSum(node, currSum):
            if node is None or currSum is None:
                return 0
            add = 0
            if currSum == targetSum:
                add +=1
            if currSum == node.val:
                visited.append([node,node.val])
            a = 0
            b = 0
            if node.left is not None:       
                if [node.left, node.left.val] not in visited:
                    a = pathSum(node.left,node.left.val if node.left else None)
            if node.right is not None:
                if [node.right, node.right.val] not in visited:
                    b = pathSum(node.right,node.right.val if node.right else None)
            return a + b + pathSum(node.left,currSum+node.left.val if node.left else None)  + pathSum(node.right,currSum+node.right.val if node.right else None) + add

        
        if root is not None:
            paths = pathSum(root,root.val)
            return paths
        else:
            return 0
