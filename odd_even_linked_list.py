class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self,head):
        curr = head
        even = None
        even_head = None
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
                        curr.next = curr.next 
                else:
                    curr.next =  even_head
                    break
            curr = curr.next