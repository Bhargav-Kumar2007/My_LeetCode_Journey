class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(l,tgt,lft=True):
            lt=0
            rt=len(l)-1
            while lt <= rt:
                mid=(lt+rt)//2
                if l[mid] < tgt:
                    lt = mid+1
                elif l[mid] > tgt:
                    rt = mid-1
                else:
                    if lft:
                        if mid==0:
                            return 0
                        elif l[mid-1] < tgt:
                            return mid
                        else:
                            rt = mid-1
                    else:
                        if mid==len(l)-1:
                            return len(l)-1
                        elif l[mid+1] > tgt:
                            return mid
                        else:
                            lt = mid+1
            return -1
        return [binary_search(nums,target,True),binary_search(nums,target,False)]
