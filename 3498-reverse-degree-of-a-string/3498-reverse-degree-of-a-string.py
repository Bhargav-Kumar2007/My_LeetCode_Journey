class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        n=1
        for i in s:
            sum+=((26-(ord(i)-97))*n)
            n+=1
        return sum