class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        mx=[]
        n=0
        for i in nums2:
            nm=0
            for j in range(-1,-n-1,-1):
                if mx[j]<i:
                    nm+=1
                else:
                    break
            for _ in range(nm):
                dic[mx.pop()]=i
                n-=1
            mx.append(i)
            n+=1
        ret=[]
        for i in nums1:
            if dic.get(i):
                ret.append(dic[i])
            else:
                ret.append(-1)
        return ret