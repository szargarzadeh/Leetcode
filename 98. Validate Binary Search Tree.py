# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            nodes.append(root.val)
            in_order(root.right)

        in_order(root)
        return nodes == sorted(nodes) and len(nodes) == len(set(nodes))
