# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root==None:
            return root
        if p==q:
            return p
        if p.val>q.val:
            return self.lowestCommonAncestor(root,q,p)
        if p.val<q.val:
            if q.val<root.val:
                return self.lowestCommonAncestor(root.left,p,q)
            elif p.val>root.val:
                return self.lowestCommonAncestor(root.right,p,q)
            else:
                return root
        