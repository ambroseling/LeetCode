class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self,head):
        curr = head
        even = None
        even_head = None
        # need to think abotu the edge cases where its all none
        if curr is None or curr.next is None or curr.next.next is None:
            return head
        while curr != None:
            if even_head is None:
                even = curr.next
                even_head = even
                curr.next = curr.next.next
                even.next = None
            else:
                even.next = curr.next
                even = even.next
                if curr.next is not None:
                    if curr.next.next is not None:
                        curr.next = curr.next.next 
                    else:
                        curr.next = even_head
                        even = None
                        break 
                else:
                    curr.next =  even_head
                    even = None
                    break
            curr = curr.next
        
        return head
