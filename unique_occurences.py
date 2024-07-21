class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occur = {}
        for i in range(len(arr)):
            if arr[i] in occur:
                occur[arr[i]] += 1
            else:
                occur[arr[i]] = 1
        if len(set(occur.values())) == len(set(arr)):
            return True
        else:
            return False
