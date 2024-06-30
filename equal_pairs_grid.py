class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nums = {}
        for i in range(len(grid)):
            row = tuple(grid[i])
            col = tuple(grid[:,i])
            if row not in nums:
                nums[row] = 1
            else:
                nums[row] += 1
            if row not in nums:
                nums[row] = 1
            else:
                nums[row] += 1
        for i in range(len(grid)):
