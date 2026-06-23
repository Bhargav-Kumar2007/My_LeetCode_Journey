class Solution:
    def isNumber(self, s: str) -> bool:

        if s.startswith("-"):
            s=s[1:]
        elif s.startswith("+"):
            s=s[1:]
        if s.startswith("-") or s.startswith("+"):
            return False
        if s.endswith("-") or s.endswith("+"):
            return False
        try:
            if not s.isalpha():
                float(s)
                return True
            else:
                return False
        except:
            return False