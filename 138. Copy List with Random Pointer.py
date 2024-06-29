"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Didn't know how copies in context of Linked Lists work.
        # the problem is actually pretty easy
        # we make a hashmap, so that we can store the relationship between
        # the old and new nodes.
        # this simplifies getting the links for each of the nodes
        old_to_curr = {None: None} # edge case, if node is pointing to None, 
                                   # This takes care of it.
        cur1, cur =head, head
        # This loop just makes and stores the nodes, 
        while cur1:
            copy = Node(cur1.val) # making a copy of the node
            old_to_curr[cur1] = copy
            cur1 = cur1.next
        
        # as you can see here, to make the links, we simple just use the 
        # stored keys as references.
        while cur:
            copy = old_to_curr[cur]
            copy.next, copy.random  = old_to_curr[cur.next], old_to_curr[cur.random]  
            cur = cur.next
        
        return old_to_curr[head]