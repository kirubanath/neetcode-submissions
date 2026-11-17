# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not subRoot:
            return True
        
        # DFS and go to each node, check value and comapre

        def compare(p,q):
            if not p and not q:
                return True
            
            if (not p and q) or (not q and p) or (p.val != q.val):
                return False
            
            left = compare(p.left, q.left)
            right = compare(p.right, q.right)

            return left and right
        
        stack = [root]

        while stack:
            node = stack.pop()

            if compare(node,subRoot):
                return True
            
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
        
        return False
            

        
