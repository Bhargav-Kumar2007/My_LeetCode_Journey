class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            if x>=-2**31 and int(str(-x)[::-1])*(-1)>=-2**31:
                return int(str(-x)[::-1])*(-1)
            else:
                return 0

        else:
            if x<=2**31 and int(str(x)[::-1])<=2**31:
                return int(str(x)[::-1])
            else:
                return 0