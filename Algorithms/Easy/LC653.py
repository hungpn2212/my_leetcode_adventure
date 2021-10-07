# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = {}
        visited = []
        def traversal(root: TreeNode):
            
            if root:
                if root.val is None:
                    return
                else:
                    visited.append(root.val)
                traversal(root.left)
                traversal(root.right)
            else:
                return
        if root.left is None and root.right is None:
            return False
        else:
            pair = 0
            traversal(root)
            for i in visited:
                res[i] = 0
                res[k-i] = 0
            for i in visited:
                pair += res[k-i]
                res[i] += 1
            return pair > 0