class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallest=nums[0]+nums[1]+nums[2]
        closeness=abs(target-smallest)
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                num=nums[i]+nums[l]+nums[r]
                if num>target:
                    if num-target<closeness:
                        smallest=num
                        closeness=num-target
                    r-=1
                elif num<target:
                    if target-num<closeness:
                        smallest=num
                        closeness=target-num
                    l+=1
                else:
                    return target
        return smallest