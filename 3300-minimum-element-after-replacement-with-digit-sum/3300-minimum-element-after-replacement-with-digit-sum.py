class Solution:
    def minElement(self, nums: List[int]) -> int:
        x=10000
        for i in nums:
            sum=0
            while i:
                sum+=i%10
                i=i//10
            if x>sum:
                x=sum
        return x