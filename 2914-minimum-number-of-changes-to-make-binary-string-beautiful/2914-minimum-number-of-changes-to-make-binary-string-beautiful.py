class Solution:
    def minChanges(self, s: str) -> int:
        c=0
        for i in range(len(s)//2):
            if s[i*2]!=s[i*2+1]:
                c+=1
        return c