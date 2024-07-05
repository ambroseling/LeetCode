# medium
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        # in a queue
        # 1) if we see a D, we pop it, and append to the start, because its still viable
        #    and at the same time increment the count of D we have seen by 1. this means that it can vote again in the next round
        # 2) Then if we see an R, and there has been count(D) >= 1, we pop the R, 
        #    and decrease the count of D by 1.
        # And put in conditions for, if len(queue) and count of (D) or (R) is same, return 
        # that.
        import collections
        q = collections.deque()
        # Fill up the queue
        for a in senate:
            q.append(a)

        countR = 0
        countD = 0

        while q:
            # get the letter
            a = q.popleft()
            if a == "R":
                if countD > 0:
                    countD -= 1
                else:
                    countR += 1
                    q.append(a)
            else:  # This means that a == "D"
                if countR > 0:
                    countR -= 1
                else:
                    countD += 1
                    q.append(a)

            # If the entire queue is processed and only one party remains
            if countR >= len(q):
                return "Radiant"
            if countD >= len(q):
                return "Dire"

# DDRRR
# DRRRD
# RRRDD
# RDD
# DDR
# DR
# RD
# D