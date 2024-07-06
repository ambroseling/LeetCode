# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#  medium.
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        intuition: 
        we do BFS, by defenition of BFS, the right most nodes should be on the right most of each of the level lists,
        in the result array.
        ex: res =  [[1], [2,3], [5,4]]
        We simply need to get the right most on each level, which will be our answer...
        """
        
        import collections
        q = collections.deque()
        res = []
        if root:
            q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
                
            res.append(level)
        result = []
        print(res)
        for i in range(len(res)):
            result.append(res[i][-1])
        return result