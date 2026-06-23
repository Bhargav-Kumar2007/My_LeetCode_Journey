class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l=[]
        ln=len(nums)
        for i in range(ln-3):
            for j in range(i+1,ln-2):
                lft=j+1
                rgt=ln-1
                while lft<rgt:
                    if nums[i]+nums[j]+nums[lft]+nums[rgt] < target:
                        lft+=1
                    elif nums[i]+nums[j]+nums[lft]+nums[rgt] > target:
                        rgt-=1
                    elif nums[i]+nums[j]+nums[lft]+nums[rgt] == target:
                        tl=[nums[i],nums[j],nums[lft],nums[rgt]]
                        if tl not in l:
                            l.append(tl)
                        rgt-=1
        return l