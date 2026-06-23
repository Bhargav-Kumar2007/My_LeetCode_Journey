class Solution:
    def compressedString(self, word: str) -> str:
        s=""
        c=0
        f=word[0]
        for i in word:
            if c==9:
                s=s+"9"+f
                c=0
            if f==i:
                c+=1
            elif f!=i and c>0:
                s=s+str(c)+f
                f=i
                c=1
            elif f!=1:
                f=i
                c=1
        s=s+str(c)+f
        return s