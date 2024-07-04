# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        mid = (n+1)//2

        if guess(high) ==0:
            return high
        if guess(low) ==0:
            return low

        # if n%2 >0:
        while guess(mid) != 0:
            mid = (high + low)//2
            if guess(mid) == -1:
                high = mid-1
                mid = (high + low)//2
            else:
                low = mid+1
   
        return mid
        
