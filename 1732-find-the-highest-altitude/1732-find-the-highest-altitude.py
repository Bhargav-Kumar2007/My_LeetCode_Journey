class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x = 0
        high = 0 
        for i in gain:
            x+=i
            if x>high:
                high = x
        return high