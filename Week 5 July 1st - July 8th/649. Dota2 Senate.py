# medium
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        """Full intiution:
        Case DDRRR:
        iter 0
        queue looks like this: 
        q = DDRRR
        countD = 0 # number of pending D bans
        countR = 0 # number of pending R bans
        
        iter 1
        pop D as no pending R bans (countR = 0), then add back at start of queue, to show they can still vote next round. countD +=1
        q = DRRRD
        countD = 1
        countR = 0

        iter 2
        pop D, as no pending R bans (countR = 0), then add back at start of queue, to show they can still vote next round. countD +=1
        q = RRRDD
        countD = 2
        countR = 0

        iter 3
        pop R, as countD > 0, AKA we have bans from D still not implemented, countD -=1
        q = RRDD
        countD = 1
        countR = 0

        iter 4
        pop R, as countD > 0, AKA we have bans from D still not implemented, countD -=1
        q = RDD
        countD = 0
        countR = 0

        iter 5
        pop R, as no pending D bans (countD = 0), then add back at start of queue, to show they can still vote next round. countR +=1 
        q = DDR
        countD = 0
        countR = 1

        iter 6
        pop D, as countR > 0, AKA we have bans from R still not implemented, countR -=1
        q = DR
        countD = 0
        countR = 0

        iter 7
        pop D, as no pending R bans (countR = 0), then add back at start of queue, to show they can still vote next round. countD +=1
        q = RD
        countD = 1
        countR = 0

        iter 8
        pop R, as countD > 0, AKA we have bans from D still not implemented, countD -=1
        q = D
        countD = 0
        countR = 0
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