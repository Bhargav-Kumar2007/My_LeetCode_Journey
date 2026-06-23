class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        fin_arr=[]
        for i in nums:
            ta=[]
            while i:
                n=i%10
                i=i//10
                ta.append(n)
            for j in ta[::-1]:
                fin_arr.append(j)
        return fin_arr
                
