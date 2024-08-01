class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l = []
        max_avg = -float('inf')
        curr_avg = 0
        if len(nums) == 1:
            return nums[0]/k
        for i in range(len(nums)):
            l.append(float(nums[i]))
            curr_avg +=float(nums[i])/k
            if len(l) == k:
                max_avg = max_avg if max_avg > curr_avg else curr_avg
                curr_avg -= float(l.pop(0))/k
        return max_avg

