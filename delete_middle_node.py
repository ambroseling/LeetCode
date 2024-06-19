class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self,head):
        curr = head
        length = 0
        while curr != None:
            length +=1
            curr = curr.next
        index = 0
        middle = (length // 2)
        if middle == 0:
            return None
        curr = head 
        while curr != None:
            if index+1 == middle:
                curr.next = curr.next.next
                break
            index += 1
            curr = curr.next
        return head

if __name__ == "__main__":
   
   a =  ListNode(val=1,next = ListNode(val=2,next=ListNode(val=2,next=None)))
   s = Solution()   
#    import ipdb;ipdb.set_trace()
   head = s.deleteMiddle(a)
   getattr(head,"next")
   print(head.next.val)

   # need to optimizer for better cuz this is O(n+n)