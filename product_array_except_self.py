class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0  
        j = len(nums)-1
        prods = [1] * len(nums)
        cumm_left = 1
        cumm_right = 1
        while i < len(nums) and j >= 0:
            prods[i] *= cumm_left
            cumm_left *= nums[i]

            prods[j] *= cumm_right
            cumm_right *= nums[j]
            i+=1
            j-=1
        return prods

