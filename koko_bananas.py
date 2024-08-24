import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        speeds = list(range(0,max(piles)+1))
        low = 0
        high = len(speeds)-1
        total = sum(piles)
        mid = (high+low) //2
        if h == len(piles):
            return max(piles)
        max_hours = 0
        min_speed = min(piles)
        # minimize speed -> 
        while low < high:
            mid = (high+low) //2
            num = -(-total// speeds[mid])
            print(num)
            print(min_speed)

            if num  <= h and speeds[mid] >= min_speed:
                min_speed = speeds[mid]
                high = mid-1
            else:
                low = mid+1
            
        return speeds[mid]


if __name__  == "__main__":
    s = Solution()
    piles = [3,6,7,11]
    h = 8
    r = s.minEatingSpeed(piles,h)
    print(r)