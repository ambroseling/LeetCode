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
    
# Others thinking
# 
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        b = {}
        ans = 0
        for i in nums:
            if k-i in b and b[k-i] > 0:
                ans+=1
                b[k-i] -=1
            elif i not in b:
                b[i] = 1
            else:
                b[i] += 1



