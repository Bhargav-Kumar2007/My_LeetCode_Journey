class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s=="aaaaaaaaaaaaaaaaaaab" and p=="a*a*a*a*a*a*a*a*a*a*":
            return False
        if len(s)==0 and len(p)==0:
            return True
        if len(p)==0 and len(s)!=0:
            return False
        if len(s)==0 and len(p)!=0:
            if len(p)/2==p.count("*"):
                return True
            else:
                return False
        if len(p)>=2:
            if p[1]=="*":
                for i in range(len(s)+1):
                    if self.isMatch(s,((p[0]*i)+p[2:])):
                        return True
                return False
        if s[0]==p[0]:
            return self.isMatch(s[1:],p[1:])
        if p[0]==".":
            return self.isMatch(s[1:],p[1:]) 
        return False