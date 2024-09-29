class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        def countTilings(n,memo):
            if n in memo: return memo[n]
            total = 0
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n >= 1:
                total += countTilings(n - 1,memo)
            if n >= 2:
                total += countTilings(n - 2,memo)
            if n >= 4:
                for i in range(1,((n-2)//2)+1):
                    total += 2 * countTilings(n - (i*2+2),memo)
            if n >= 3:
                for i in range(1,((n-1)//2)+1):
                    total += 2 * countTilings(n - (i*2+1),memo)
            memo[n] = total
            return total
        memo = {}
        return int(countTilings(n,memo) % (1e9 + 7))




if __name__ == "__main__":
    s = Solution()
    print(s.numTilings(50))