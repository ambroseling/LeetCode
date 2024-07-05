class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        count_r = 0
        count_d = 0
        senate = list(senate)
        while len(set(senate)) > 1:

            if senate[0] == "R":
                if count_d == 0:
                    # there are no bans from d
                    count_r +=1
                    senate.append(senate.pop(0))
                else:
                    # there are bans from d

                    count_d -=1
                    senate.pop(0)
                    
            else:
                if count_r == 0:
                    count_d +=1
                    senate.append(senate.pop(0))
                else:
                    count_r -=1
                    senate.pop(0)
    
        return "Radiant" if list(set(senate))[0]== "R" else "Dire"


