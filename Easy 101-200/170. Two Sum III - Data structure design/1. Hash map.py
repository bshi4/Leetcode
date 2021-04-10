class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.dict = {}
        
    def add(self, number):
        if number not in self.dict:
            self.dict[number] = 1
        else:
            self.dict[number] += 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        for n in self.dict:
            diff = value - n
            if diff in self.dict and (diff != n or self.dict[diff] > 1):
                return True
        return False
        
        