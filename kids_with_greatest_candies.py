class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        orig_max = max(candies)
        largest_kid = []
        for kid_candy in candies:
            if kid_candy+extraCandies >= orig_max:
                largest_kid.append(True)
            else:
                largest_kid.append(False)
        return largest_kid
