class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        max=dic[s[-1]]
        tot=0
        for i in s[::-1]:
            if dic[i] < max:
                tot-=dic[i]
                continue
            if dic[i] > max:
                max=dic[i]
                tot+=dic[i]
                continue
            tot+=dic[i]
        return tot