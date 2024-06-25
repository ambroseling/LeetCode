class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves_1 = []
        leaves_2 = []
        def getLeaves(node,leaves):
            if node.left is None and node.right is None:
                leaves.append(node.val)
                return
            else:
                if node.left is not None:
                    getLeaves(node.left,leaves)
                
                if node.right is not None:
                    getLeaves(node.right,leaves)
                else:
                    return

        
        if root1 is None:
            pass
        elif root1.left is None and root1.right is None:
            leaves_1.append(root1.val)
        else:
            getLeaves(root1,leaves_1)

        if root2 is None:
            pass
        elif root2.left is None and root2.right is None:
            leaves_2.append(root2.val)
        else:
            getLeaves(root2,leaves_2)
        

        if len(leaves_1) != len(leaves_2):
            return False
        else:
            same = True
            for i in range(len(leaves_1)):
                if leaves_1[i] != leaves_2[i]:
                    same = False
                    break
            return same