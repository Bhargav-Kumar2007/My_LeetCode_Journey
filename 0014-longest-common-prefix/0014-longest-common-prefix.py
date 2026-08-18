class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def comm(s1,s2):
            pref=s1
            for i in s1:
                if s2.startswith(pref):
                    return pref
                pref = pref[:-1]
            return pref
        count=0
        for i in strs:
            count+=1
        if count==1:
            return strs[0]
        if count==0:
            return ""
        pref=comm(strs[0],strs[1])
        for i in range(2,count):
            pref=comm(pref,strs[i])
        return pref