import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        neg = [0]*1000
        pos = [0]*1000
        top = []
        for num in nums:
            if num > 0:
                pos[num] +=1
            else:
                num = num * -1
                neg[num]+=1
        for i in range(len(neg)):
            heapq.heappush(top,(-neg[i],-i))
        for i in range(1,len(pos)):
            heapq.heappush(top,(-pos[i],i))
        return [heapq.heappop(top)[1] for i in range(k)]
