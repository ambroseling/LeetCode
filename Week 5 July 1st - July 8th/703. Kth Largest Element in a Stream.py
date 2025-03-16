class KthLargest(object):
    import heapq
    # it will be n log n, as if k is very small, we will have to pop all but 1 elements.
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
    # our time complexity is:
    # O(logn) for adding, as we remove and add 1 element.
    def add(self, val):
        # we add the new element the heap readjusts
        heapq.heappush(self.minHeap, val)        
        if len(self.minHeap) > self.k:
            # we got more elements, we simple pop till we have the kth largest (AKA the smallest in the heap)
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)