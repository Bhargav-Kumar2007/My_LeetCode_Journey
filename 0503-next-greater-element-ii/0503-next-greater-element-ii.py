class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        dic={}
        ls=[]
        n=0
        ln=0
        for _ in nums:
            ln+=1
        for i in range(ln):
            while n>0:
                if nums[ls[-1]]<nums[i]:
                    dic[ls.pop()]=nums[i]
                    n-=1
                else:
                    break
            ls.append(i)
            n+=1
        for i in range(ln):
            if n==1:
                break
            while n>0:
                if nums[ls[-1]]<nums[i]:
                    dic[ls.pop()]=nums[i]
                    n-=1
                else:
                    break
        res=[]
        for i in range(ln):
            res.append(dic.get(i,-1))
        return res