# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. base case: if root is None, return None
        # 2. do the work at this node (your swap)
        # 3. call invertTree on the children
        # 4. return root
        
        if root is None:
            return None
        else:
            s = root.right
            root.right = root.left
            root.left = s
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

        