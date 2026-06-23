class Solution:
    def sortVowels(self, s: str) -> str:
        x=[]
        vow=[]
        s=[i for i in s]
        for i,a in enumerate(s):
            if a in "aeiouAEIOU":
                x.append(i)
                vow.append(a)
        vow.sort()
        for i in range(len(vow)):
            s[x[i]]=vow[i]
        z=""
        for i in s:
            z+=i
        return z