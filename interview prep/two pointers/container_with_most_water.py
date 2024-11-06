
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_volume = 0

        while left < right:
            # idea is you always move the pointer with the smaller height
            volume = min(height[left],height[right]) * (right-left)
            max_volume = max(max_volume, volume)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1

        return max_volume