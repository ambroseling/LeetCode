class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        #iterate through the array and calculate the prefix
        # we are calculating the prefix for each element
        # res[i] stores the product of all the elements to the left of the current element
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        #calculate the postfix
        # we are calculating the postfix for each element
        # res[i] mulitplies the product of all the elements to the right of the current element on top of the prefix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

# main idea is to use prefix and postfix to calculate the product of the array except for the current element
# prefix is the product of all the elements to the left of the current element
# postfix is the product of all the elements to the right of the current element
# the result array is the product of the prefix and postfix