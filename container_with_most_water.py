class Solution(object):
    def maxArea(self,arr):
        left = 0
        right = len(arr)-1
        mvolume = 0 
        while left < right:
            volume = 0
            if right-1 >0 and (right - 1 - left) * (arr [left] if arr[left] < arr[right-1] else arr[right-1]) > mvolume:
                right -=1
                volume = (right - left) * ( arr [right] if arr[right] < arr[left] else arr[left] )

            elif left + 1 < len(arr)-1 and (right - (left + 1) ) * (arr [right] if arr[right] < arr[left+1] else arr[left+1]) > mvolume:
                left +=1
                volume = (right - left) * ( arr [right] if arr[right] < arr[left] else arr[left] )
            else:
                if arr[left] > arr[right]:
                    right -= 1
                else:
                    left+=1

                
            if volume >= mvolume:
                mvolume = volume

        return mvolume
    
# Their thinking
# assume that the larger height always leads to larger area, which shd be true
# so theres no need to compare the current volume with the next volume
# so just assume higher height leads to bigger volume

while left < right:
    volume = min(height[left],height[right]) * (right-left)
    if height[left] < height[right]:
        left +=1
    else:
        right -=1