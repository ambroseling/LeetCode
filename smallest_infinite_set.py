class SmallestInfiniteSet(object):

    def __init__(self):
        self.infset = [0] * 1000
        for i in range(1000):
            self.infset[i] = i

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.infset[1] < self.infset[2]:
            # swap with the samller child
            i = 0
            while 2*i+1 < len(self.infset):
                (self.infset[2*i+1],self.infset[i]) = (self.infset[i],self.infset[2*i+1])
                i = 2*i+1
            self.infset.pop(-1)
        else:
            i = 0
            while 2*i+2 < len(self.infset):
                (self.infset[2*i+2],self.infset[i]) = (self.infset[i],self.infset[2*i+2])
                i = 2*i+2
            self.infset.pop(-1)

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.infset:
            self.infset.append(num-1)
            i = len(self.infset)-1
            while self.infset[(i-1)/2] > self.infset[i]:
                (self.infset[(i-1)/2],self.infset[i]) = (self.infset[i],self.infset[(i-1)/2])
                i = (i-1)/2
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

# Min heap datastructure
# - a[(i-1)/2] gives you parent of node i 
# - a[2i +1] gives you left child of node i
# - a[2i +2] gives you right child of node i

if __name__ == "__main__":
    s = SmallestInfiniteSet()
    s.popSmallest()