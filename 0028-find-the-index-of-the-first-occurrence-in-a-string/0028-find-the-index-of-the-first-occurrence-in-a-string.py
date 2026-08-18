class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lns1=0
        for _ in haystack:
            lns1+=1
        lns2=0
        for _ in needle:
            lns2+=1
        if haystack==needle:
            return 0
        for i in range(lns1-lns2+1):
            fl=0
            for j in range(lns2):
                if haystack[i+j]!=needle[j]:
                    fl=1
                    break
            if fl==0:
                return i
        return -1

            
