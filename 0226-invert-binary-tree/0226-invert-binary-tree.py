# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        def inverter(a):
            a.left,a.right=a.right,a.left
            if a.left:
                inverter(a.left)
            if a.right:
                inverter(a.right)
        inverter(root)
        return root