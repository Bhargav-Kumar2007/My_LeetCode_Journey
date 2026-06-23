class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=""
        j=""
        for i in s:
            if i.isdigit():
                l+=i
            elif (j.isdigit()==True or j=="+") and i.isdigit()==False:
                break
            elif i==" ":
                pass
            elif j=="-" and i=="+":
                break
            elif j=="+" and i=="-":
                break
            elif i=="+" or i=="-":
                l+=i
            else:
                break
            j=i
        try:
            if int(l) >= 2**31:
                return 2**31-1
            elif int(l) <= -2**31:
                return -2**31
            else:
                return int(l)
        except:
            return 0