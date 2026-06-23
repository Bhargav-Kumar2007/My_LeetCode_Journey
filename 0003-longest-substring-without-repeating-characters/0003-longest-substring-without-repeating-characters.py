class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        for i in range(len(s)):
            ss=""
            for j in s[i:]:
                if j not in ss:
                    ss+=j
                else:
                    break
            if len(ss)>l:
                l=len(ss)
        return l
