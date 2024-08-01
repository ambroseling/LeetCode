class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """


        nums = sorted(list(zip(nums1,nums2)),key=itemgetter(1),reverse=True) # O(N)
        max_sum = 0
        prefixSum = 0
        heap = []
        for a,b in nums:
            prefixSum += a
            heappush(heap,a)
            if len(heap) == k:
                max_sum = max(max_sum,prefixSum*b)
                prefixSum -= heappop(heap)
        return max_sum

