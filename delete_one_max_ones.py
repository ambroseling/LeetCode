# My attempt: yuck
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        n,l,r = len(nums),0,0
        latest_zero = 0
        ones = 0
        count = 0
        recent_sum = 0
        max_ones = 0
        import ipdb; ipdb.set_trace(context = 10)
        while r < n:
            if nums[r] == 0:
                if count ==0:
                    count +=1
                    recent_sum = ones
                else:
         
                    if r - latest_zero> 1 :
                        max_ones = max(max_ones,ones)
                    if r< len(nums)-1 and nums[r+1] == 1:
                        recent_sum = ones
                        ones -= recent_sum
                latest_zero = r
            else:
                ones +=1 
            r +=1
        print(max_ones,ones)
        if count == 0:
            #that means no 0s
            max_ones = max(max_ones,ones)
            return max_ones - 1
        elif count == 1: #only 1 zero
            max_ones = max(max_ones,ones)
            return max_ones
        else:
            return max_ones

if __name__ == "__main__":
    s = Solution()
    arr = [0,1,1,1,0,0,1,1,0]
    r = s.longestSubarray(arr)
    print(r)

# How to understand others solution:
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero_count = 0
        longest_window = 0
        start = 0
        for i in range(len(nums)):
            zero_count += nums[i] == 0
            while zero_count > 1: 
                zero_count -= (nums[start] == 0)
                start += 1
            longest_window  = max(longest_window,i=start)
        return longest_window
        