import math
class Solution:
    def constructRectangle(self, area):
        x = int(math.sqrt(area))
        
        if x*x == area:
            return [x,x]
        else:
            if area % x != 0:
                x -= 1
            else:
                return [area/x, x]
        
        