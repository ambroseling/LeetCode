class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        l = 0 
        r = 0
        num_ones = 0
        import ipdb; ipdb.set_trace(context = 10)
        for r in range(n):
            if nums[r] == 0: # if the number we are  on is a 0
                if k == 0: # if you flipped k 0s already, its time to roll your L pointer forward to count how many consecutive ones are there
                    while nums[l] !=0: l +=1 
                    l+=1
                else: #if the right pointer is seeing a 1 (dont satisfy our condition)
                    k -=1 
            num_ones = max(num_ones,r-l+1)
        return num_ones
                
if __name__ == "__main__":
    arr = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    s = Solution()
    num = s.longestOnes(arr,3)
    print(num)