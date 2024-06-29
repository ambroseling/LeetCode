# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            # idea 1: Dumbass solution
            # we can simply reverse the list, and then traverse it, and remove the n'th 
            # element, then reverse again. 

            # idea 2: we use 2 pointers, first one gets the length, the 
            # second one goes to len-n and removes the node, 
            # and then simply returns the head.

            # Optimal !!!!!
            # idea 3: we can make 2 pointers (p1, p2), the p1 goes n infront of p2, 
            # then we let both continue till p1 is null, 
            # because p1 is n in front, p2 is what we remove
            
            dummy,l, r = head, head, head 
            counter = 0
            while counter < n :
                r = r.next
                counter +=1
            
            # edge case, if r is None (meaning we are removing the first element):
            if r is None:
                dummy= dummy.next
                return dummy
            
            # otherwise:        
            while r.next is not None: 
                l = l.next
                r = r.next

            # now r is on final one, and l is one before the node we want to remove.
            l.next = l.next.next
            return dummy

            




            
            
