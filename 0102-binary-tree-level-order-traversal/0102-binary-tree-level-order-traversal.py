# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        ls=[root]
        ret=[]
        while ls:
            tret=[]
            tls=[]
            for i in ls:
                tret.append(i.val)
                if i.left:
                    tls.append(i.left)
                if i.right:
                    tls.append(i.right)
            ret.append(tret)
            ls=tls
        return ret