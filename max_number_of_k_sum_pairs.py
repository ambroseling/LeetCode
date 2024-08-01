class Solution(object):
    def maxOperations(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(arr)-1
        ops = 0
        occur = {}
        for i in range(len(arr)):
            if arr[i] < k:
                if arr[i] in occur:
                    occur[arr[i]] +=1
                else:
                    occur[arr[i]] = 1
                if( arr[i] in occur and (k-arr[i]) in occur and occur[arr[i]] >= 1 and occur[k-arr[i]]>= 1 and arr[i] != k-arr[i] ) or (arr[i] == k-arr[i] and occur[arr[i]] ==2 and k//2 == arr[i]):
                    ops +=1
                    occur[arr[i]] = occur[arr[i]] - 1
                    occur[k-arr[i]] = occur[k-arr[i]] - 1 if k-arr[i] in occur else 0

        return ops