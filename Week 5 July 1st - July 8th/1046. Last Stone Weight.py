class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # complexity:
        # each iteration takes O(logn) time
        # we should have n iterations (0 stones left)
        # therefore complextiy is O(nlogn)
        stones = [-s for s in stones] # python dont have max heaps, 
                                      # so (-) everything in min heap = max heap 
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: # as we negated every weight
                heapq.heappush(stones,  (first - second))
        stones.append(0) # in case our heap is empty
        return abs(stones[0])
     