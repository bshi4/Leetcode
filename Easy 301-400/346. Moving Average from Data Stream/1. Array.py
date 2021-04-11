class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        self.list = []
        self.sum = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        self.list.append(val)
        self.sum += val
        if len(self.list) > self.size:
            self.sum -= self.list.pop(0)
        return self.sum/len(self.list)
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)