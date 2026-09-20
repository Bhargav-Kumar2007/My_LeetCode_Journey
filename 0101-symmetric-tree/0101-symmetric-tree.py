# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def sym(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return sym(p.left,q.left) and sym(p.right,q.right)
        def rev(n):
            n.left,n.right=n.right,n.left
            if n.left:
                rev(n.left)
            if n.right:
                rev(n.right)
        if not root:
            return True
        if root.left:
            rev(root.left)
        return sym(root.left,root.right)
