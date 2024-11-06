class  Solution():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                return [left, right]

        return []