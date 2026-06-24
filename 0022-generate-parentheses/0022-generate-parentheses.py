class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st={"()"}
        if n==1:
            return list(st)
        for i in range(n-1):
            ts=set()
            for j in st:
                lnj=len(j)
                for k in range(lnj):
                    x=j[0:k]+"()"+j[k:]
                    ts.add(x)
            st=ts
        return list(st)
