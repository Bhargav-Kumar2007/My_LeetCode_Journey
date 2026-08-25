class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ln=0
        sm=0
        for i in nums:
            ln+=1
            sm+=i
        s=ln*(ln+1)//2
        return s-sm
