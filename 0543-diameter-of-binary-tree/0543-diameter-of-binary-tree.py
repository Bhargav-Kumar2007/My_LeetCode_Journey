# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    bst=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def counter(n):
            if not n:
                return 0
            l=counter(n.left)
            r=counter(n.right)
            self.bst=max(self.bst,l+r)
            return 1+max(l,r)
        counter(root)
        return self.bst