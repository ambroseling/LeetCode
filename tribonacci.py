class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        def tri(num):
            if num <= 3:
                return 2
            return tri(num -1) + tri(num-1) + tri(num-2)
        num =  tri(n)
        return num
    


if __name__ == "__main__":
    s = Solution()
    r = s.tribonacci(4)
    print(r)