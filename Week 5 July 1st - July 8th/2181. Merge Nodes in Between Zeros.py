# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# medium
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        '''
        You can easily solve using new nodes, 
        this solution does it in place with time complexity of O(n) and memory of O(1), as we dont use extra, its in place.
        Intuition: 
        4 pointers in total, 
        head: the one we iterate over, 
        res: this is the one that changes the original list into the sum'ed version
        prev: we use this to cut off the rest of the LinkedList
        dummy: we use this to return the head of the modified linkedL
        '''

        prev, res, dummy =head, head, head
        res = res.next
        head = head.next
        counter = 0
        while head:
            if head.val == 0:
                res.val = counter
                prev = prev.next
                res = res.next
                head = head.next
                counter = 0
            else:
                counter += head.val
                head = head.next 
        prev.next = None
        dummy = dummy.next
        return dummy