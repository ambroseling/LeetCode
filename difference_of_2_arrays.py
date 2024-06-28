class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        num1 = set(nums1)
        num2 = set(nums2)
        answer = []
        answer.append(list(num1.difference(num2)))
        answer.append(list(num2.difference(num1)))
        return answer
        