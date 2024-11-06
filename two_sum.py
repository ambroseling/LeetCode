class Solution:
    def twoSum(self, nums, target: int):
         import ipdb; ipdb.set_trace()
         nums = sorted(nums)
         for i in range(len(nums)-1):
            low = i+1
            high = len(nums)-1
            while low < high:
                mid = (low + high) // 2
                if nums[mid] + nums[i] < target:
                    low = mid+1
                else:
                    high = mid
            if nums[i] + nums[low] == target:
                return [i,low]


if __name__ == "__main__":
    s = Solution()
    nums = [3,2,4]
    nums = [2,3,4]
    result = s.twoSum(nums,6)