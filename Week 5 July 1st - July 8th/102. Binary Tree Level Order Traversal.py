# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Medium
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        intuition:
        The queue at each iteration contains the nodes for each level, 
        That is why we add in the root node at the start.
        Then, at each iteration, (starting at level 1, for root node is already in queue)
        We pop the nodes in the for loop, and appened each of them to level list.
        Then, because we have already set the length of the queue for the for loop, 
        adding more nodes to the end of the queue doesn't effect our for loop.
        Then, as we append the node to level list, we also check for children and appened them from left to right.
        Finally append the level list to the total result list.
        """

        import collections
        q = collections.deque()
        if root: 
            q.append(root)
        result = []
        while q:
            # nodes at that level
            level = []
            # we go through the entire queue
            for i in range(len(q)): # length of queue is set from previous level (ie the # of children of that level = # of nodes in next level right )
                # getting the node at the level
                node = q.popleft()
                level.append(node.val) # adding node's value in

                # We then have to add in the children, in to the queue, 
                # So that in the next iteration that can be accounted for
                if node.left: # making sure the node is not Null/None
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result