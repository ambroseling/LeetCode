# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def search(node):
            if node is None:
                return None
            if node.left and node.left.val == key:
                delete(node,node.left,"left")
                return None
            if node.right and node.right.val == key:
                delete(node,node.right,"right")
                return None
            if key < node.val:
                return search(node.left)
            if key > node.val:
                return search(node.right)
        

        def delete(parent,node,dir):
            # if its to the left
            if dir =="left":
                if node.left is None and node.right is None:
                    parent.left = None
                elif node.right is None:
                    parent.left = node.left
                else: 
                    parent.left = node.right
                    curr = node.right

                    temp = node
                    while(curr.left != None):
                        curr = curr.left
                    curr.left = temp.left
                return 
            elif dir == "right":
                if node.left is None and node.right is None:
                    parent.right = None
                elif node.left is None:
                    parent.right = node.right
                else:
                    parent.right = node.left
                    curr = node.left
                    temp = node
                    while(curr.right !=None):
                        curr = curr.right
                    curr.right = temp.right
                return 
            else:
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left
                temp = root.left 
                new_root = root.right
                curr = root.right
                while (curr.left !=None):
                    curr = curr.left
                curr.left = temp
                return new_root

        if root is None:
            return None
        elif root.val == key:
            if root.left is None and root.right is None:
                return None
            else:
                root = delete(root,None,"root")
                return root
        else:
            result = search(root)
            return root
        