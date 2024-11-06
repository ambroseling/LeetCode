class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


# main idea is to use a hash map to store the value and its index
# iterate through the array and check if the difference between the target and the current value is in the hash map
# if it is, return the index of the difference and the current index
# if not, add the current value and its index to the hash map





prevmaps = {}
for i in range(len(nums)):
    diff = target - nums[i]
    # if the difference is in the hash map, return the index of the difference and the current index
    if diff in prevmaps:
        return [prevmaps[diff], i]
    prevmaps[nums[i]] = i



# go through each number in the array 
# calculate th edifference 
# if the difference exists in the hash mapwe return the value and the current index
# if not, we add the current value and its index to the hash map