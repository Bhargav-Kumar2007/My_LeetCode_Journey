class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        x={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        l=[]
        for i in digits:
            if l==[]:
                for j in x[i]:
                    l.append(j)
            else:
                tl=[]
                for j in l:
                    for k in x[i]:
                        tl.append(j+k)
                l=tl
        return l