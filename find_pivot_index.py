class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        most_left_index = len(nums)-1
        left_sum = 0
        right_sum = 0
        for i in range(len(nums)):
            if i in nums_dict:
                nums_dict[i] = nums_dict[i] + left_sum
            else:
                nums_dict[i] = left_sum
            if len(nums)-i-1 in nums_dict:
                nums_dict[len(nums)-i-1] = nums_dict[len(nums)-i-1] -right_sum
            else:
                nums_dict[len(nums)-i-1] = right_sum
            left_sum += nums[i]
            right_sum += nums[len(nums)-i-1]
            if i != 0 or i != len(nums)-1:
                if nums_dict[i] == 0:
                    if i < most_left_index:
                        most_left_index =i
                if nums_dict[len(nums)-i-1] == 0:
                    if len(nums)-i-1 < most_left_index:
                        most_left_index = len(nums)-i-1
        print(nums_dict)
        return most_left_index 
