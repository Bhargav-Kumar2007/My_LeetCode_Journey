# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root:
            ls=[root]
        else:
            return []
        res=[]
        flag=0
        while ls:
            tres=[]
            for i in ls:
                tres.append(i.val)
            if flag==0:
                res.append(tres)
                flag=1
            else:
                res.append(tres[::-1])
                flag=0
            tls=[]
            for i in ls:
                if i.left:
                    tls.append(i.left)
                if i.right:
                    tls.append(i.right)
            ls=tls
        return res
