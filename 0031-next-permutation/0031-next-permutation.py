class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        ln=0
        for _ in nums:
            ln+=1
        i=-1
        flag=0
        while i >= -ln+1:
            if nums[i]>nums[i-1]:
                flag=1
                break
            i-=1
        i-=1
        if flag:
            j=-1
            while j>i:
                print(j)
                if nums[j]>nums[i]:
                    break
                j-=1
            nums[j],nums[i]=nums[i],nums[j]
            print(i,j)
            nums[i+1:]=nums[i+1:][::-1]
            print(nums[:i+1],nums[i+1:])
        else:
            for x in range(ln//2):
                nums[x],nums[ln-x-1]=nums[ln-x-1],nums[x]