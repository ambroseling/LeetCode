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
        potions = sorted(potions)
        successful_spell = []
        for i in range(len(spells)):
            low = 0
            high = len(potions)-1
            # 1 2 3 4 5 
            if potions[high]*spells[i] < success:
                successful_spell.append(0)
                continue
            if potions[low]* spells[i] > success:
                successful_spell.append(len(potions))
                continue 
            # low high
            # 0   2
            # 0   1
            while low <= high:
                mid = (high+low) // 2
                # too big
                if potions[mid]*spells[i] >= success:
                    high = mid-1
                else: #potions[mid]*spells[i] < success
                    low = mid + 1
            successful_spell.append(len(potions)-low)
        return successful_spell

