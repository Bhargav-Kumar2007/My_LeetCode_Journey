# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxdiff=0
    def isBalanced(self, root: TreeNode | None) -> bool:
        def counter(n):
            if not n:
                return 0
            l=counter(n.left)
            r=counter(n.right)
            if l>=r:
                diff=l-r
            else:
                diff=r-l
            self.maxdiff=max(self.maxdiff,diff)
            return 1+max(l,r)
        counter(root)
        if self.maxdiff>1:
            ans=False
        else:
            ans=True
        self.maxdiff=0
        return ans