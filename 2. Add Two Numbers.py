# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1: Dumbass solution:
        # reverse the lists, and add them (kanye smh)

        # 2: Smarter:
        # add each one, and every time you do next, multiple by 10^# of times you do next.
        # this way you get place values, and simply add in the end

        l, r = l1, l2
        res = 0
        counter=1
        while l1 or l2:
            if l1 and l2:
                res += counter*(l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next
            elif l1 and l2 is None:
                res += counter*(l1.val)
                l1 = l1.next
            else:
                res += counter*(l2.val)
                l2 = l2.next
            counter *= 10
        
        # Forgot: need to update the first number, 
        # before assigning it to another result. As that
        # stores the defualt value of 0
        nums = str(res)[::-1]
        dummy = ListNode(0)
        dummy.val = nums[0]
        result = dummy # now the head has the same value as the first element
                       # in the dummy.
        
        for i in range(len(nums)-1):
            print(f"this is nums[i]: {nums[i]}")
            dummy.val = nums[i]

            if i == (len(nums)-1):
                dummy = dummy
            else:
                dummy.next = ListNode(nums[i+1], None)
                dummy = dummy.next


            
        return result    