class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [None for _ in range(k)]
        self.capacity = k
        self.front = 0
        self.rear = k -1
        self.size = 0

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1 
        return True    
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1 + self.capacity ) % self.capacity 
        self.size -=1
        return True


    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.rear = ( self.rear - 1 ) % self.capacity
        self.size -=1 
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.queue[self.front]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.queue[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0 

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.capacity

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()