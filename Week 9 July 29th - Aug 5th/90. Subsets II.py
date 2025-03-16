class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # nums = set(nums)
        res = []
        nums.sort()

        subset = []

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)
            # decision NOT to include nums[i]
            subset.pop()
            while i+1  < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subset)
        dfs(0,subset)

        return res