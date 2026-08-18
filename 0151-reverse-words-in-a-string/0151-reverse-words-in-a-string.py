class Solution:
    def reverseWords(self, s: str) -> str:
        ret=[]
        word=''
        for i in s:
            if i==" ":
                if word=='':
                    continue
                ret+=[word]
                word=''
                continue
            word=(word + i)
        if word!='':
            ret+=[word]
        sentence=ret[0]
        for i in ret[1:]:
            sentence=i+" "+sentence
        return sentence
            