class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        
    # rough plan:
    # 1. sort the potions
    # 2. do binary search to find starting from which strength would result in success
    # 3. counts how many potions with >= that strength, store in array
