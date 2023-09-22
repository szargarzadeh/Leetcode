# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        anc_dict = defaultdict(lambda: [])

        def helper(root):
            if not root:
                return

            anc_dict[root].append(root)
            if root.left:
                anc_dict[root.left].extend(anc_dict[root])
            if root.right:
                anc_dict[root.right].extend(anc_dict[root])
            helper(root.left)
            helper(root.right)

        helper(root)
        p_anc = anc_dict[p]
        q_anc = anc_dict[q]
        for i in range(min(len(p_anc), len(q_anc))):
            if p_anc[i] != q_anc[i]:
                return p_anc[i - 1]

        if len(p_anc) < len(q_anc):
            return p_anc[-1]
        else:
            return q_anc[-1]
