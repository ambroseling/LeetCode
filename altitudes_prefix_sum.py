class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        p_sum = 0
        largest = p_sum
        for ngain in gain:
            p_sum += ngain
            if p_sum > largest:
                largest = p_sum
        return largest
        