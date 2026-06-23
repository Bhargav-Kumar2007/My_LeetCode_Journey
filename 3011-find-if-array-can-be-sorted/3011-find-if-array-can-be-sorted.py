class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            c=None
            for j in range(len(nums)):
                if not c:
                    pass
                elif c>nums[j]:
                    if bin(c).count("1")==bin(nums[j]).count("1"):
                        nums[j],nums[j-1]=c,nums[j]
                    else:
                        return False
                c=nums[j]
        return True