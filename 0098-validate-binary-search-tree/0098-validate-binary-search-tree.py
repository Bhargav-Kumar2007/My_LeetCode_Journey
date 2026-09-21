# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    flag=True
    def isValidBST(self, root: TreeNode | None) -> bool:
        tp=root.val
        def isValid(n,low=None,high=None):
            if not(low is None):
                self.flag = self.flag and (n.val > low)
            if not(high is None):
                self.flag = self.flag and (n.val < high)
            if n.left:
                if not (high is None):
                    isValid(n.left,low,min(n.val,high))
                else:
                    isValid(n.left,low,n.val)
            if n.right:
                if not (low is None):
                    isValid(n.right,max(n.val,low),high)
                else:
                    isValid(n.right,n.val,high)
        isValid(root)
        ans=self.flag
        self.flag=True
        return ans