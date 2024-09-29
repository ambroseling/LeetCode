# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#          nums = sorted(nums)
#          for i in range(len(nums)-1):
#             low = i+1
#             high = len(nums)-1
#             while low < high:
#                 mid = (low + high) // 2
#                 if nums[mid] + nums[i] < target:
#                     low = mid+1
#                 else:
#                     high = mid
#             if nums[i] + nums[low] == target:
#                 return [i,low]


