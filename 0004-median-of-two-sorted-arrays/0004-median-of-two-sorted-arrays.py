class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j=0,0
        nums=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                nums.append(nums1[i])
                i+=1
            elif nums1[i]>=nums2[j]:
                nums.append(nums2[j])
                j+=1
        if i<len(nums1):
            nums+=nums1[i:]
        else:
            nums+=nums2[j:]
        
        x=len(nums)
        if x%2==0:
            return (nums[x//2-1]+nums[x//2])/2
        else:
            return (nums[x//2])