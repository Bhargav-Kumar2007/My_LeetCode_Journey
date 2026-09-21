# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        ti=TreeNode(val)
        if not root:
            return ti
        dummy=root
        while dummy:
            if val > dummy.val:
                if dummy.right:
                    dummy=dummy.right
                else:
                    dummy.right = ti
                    return root
            else:
                if dummy.left:
                    dummy=dummy.left
                else:
                    dummy.left = ti
                    return root