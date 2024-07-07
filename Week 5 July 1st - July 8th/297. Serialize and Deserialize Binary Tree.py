# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # simply, do a preorder traversal, and store each node , along side the null values.
        self.res = []
        def dfs (node):
            if not node: 
                self.res.append("N")
                return
            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(self.res) # makes a string, of the list



    # reverse of what we did earlier, we simply do a dfs and make the nodes as we go
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        val = data.split(",")
        self.i = 0

        def dfs():
            # getting the null out.
            if val[self.i] == "N":
                self.i += 1
                return None
            # make a node for the value
            node = TreeNode(int(val[self.i])) 
            self.i += 1
            node.left = dfs() # no need to pass anything in due to self.i
            node.right = dfs()
            return node
        return dfs() 

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))