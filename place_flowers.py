class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if len(flowerbed) > 1:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                n-=1
                flowerbed[0] = 1

            for i in range(1,len(flowerbed)-1):
                prev = i-1
                curr = i
                nxt = i+1
                if flowerbed[curr] == 0 and flowerbed[prev] == 0 and flowerbed[nxt] == 0:
                    
                    n -=1
                    flowerbed[curr] = 1
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                n -=1
                flowerbed[-1] = 1
            if n > 0:
                return False
            else:
                return True
        else:
            if flowerbed[0] == 1:
                return False
            else:
                return True
                    
