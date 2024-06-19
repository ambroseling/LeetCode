class RecentCounter(object):

    def __init__(self):
        self.pings = []


    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if len(self.pings) == 0:
            self.pings.append(t)
        elif t - self.pings[0] > 3000:
            while len(self.pings) > 0 and t - self.pings[0] > 3000:
                self.pings.pop(0)
            self.pings.append(t)
        elif t - self.pings[0] <= 3000:
            self.pings.append(t)
        return len(self.pings)


if __name__ == "__main__":
    obj = RecentCounter()
    param = obj.ping(1)


# Main take away is that not just the first element in the queue satisfies the condition
# you need to pop all the things that 
# 