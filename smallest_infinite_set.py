class SmallestInfiniteSet(object):

    def __init__(self):
        self.infset = [0] * 1000
        for i in range(1000):
            self.infset[i] = i+1

    def heapify(self,i):
        smallest = i
        left = 2*i+1
        right = 2*i+2
        if left < len(self.infset) and self.infset[left] < self.infset[smallest]:
            smallest = left
        if right < len(self.infset) and self.infset[right] < self.infset[smallest]:
            smallest = right
        if smallest != i: # perform the swap
            self.infset[i], self.infset[smallest] = self.infset[smallest], self.infset[i]
            self.heapify(smallest)


    def popSmallest(self):
        """
        :rtype: int
        """
        if len(self.infset) == 0:
            return None
        else:
            smallest = self.infset[0] # gets the smallest node in the heap (current root)
            last_element = self.infset.pop() # remove the last element ()
            self.infset[0] = last_element # 
            self.heapify(self.infset)
            return smallest




    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        if num not in self.infset:
            self.infset.append(num)
            i = len(self.infset)-1 
            while self.infset[(i-1)//2] > self.infset[i] and i > 0:
                (self.infset[(i-1)//2],self.infset[i]) = (self.infset[i],self.infset[(i-1)//2])
                i = (i-1)//2
        
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
    import ipdb; ipdb.set_trace()
    for i in range(1000):
        o = s.popSmallest()
        print(o)



