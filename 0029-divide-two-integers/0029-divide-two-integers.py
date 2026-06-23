class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ret = (dividend//divisor if divisor*dividend>0 else -(-dividend//divisor))
        if ret>=2**31-1:
            return 2**31-1
        elif ret<=-2**31:
            return -2**31
        return ret