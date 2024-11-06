class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort the array
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            # every value is a possible starting value, but we skip duplicates

            # if the current value is the same as the previous value, we skip it, that means there is a duplicate
            if i > 0 and a == nums[i - 1]:
                continue

            # do 2 pointers approach to find the other 2 numbers
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: # if the sum is greater than 0, we need to decrease the sum, so we move the right pointer to the left
                    r -= 1
                elif threeSum < 0: # if the sum is less than 0, we need to increase the sum, so we move the left pointer to the right
                    l += 1
                else: # if the sum is 0, we have found a triplet
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # skip duplicates
                        l += 1
                        
        return res
