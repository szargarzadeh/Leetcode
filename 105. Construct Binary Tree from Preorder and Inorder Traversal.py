# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def helper(preorder, inorder):
            if not preorder:
                return
            root_val = preorder[0]
            idx = inorder.index(root_val)

            root = TreeNode(root_val)
            root.left = helper(preorder[1:idx + 1], inorder[:idx])
            root.right = helper(preorder[idx + 1:], inorder[idx + 1:])
            return root

        return helper(preorder, inorder)