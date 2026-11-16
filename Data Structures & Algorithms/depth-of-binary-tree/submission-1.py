# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 1
        que = deque([(root,1)])

        while que:
            node,level = que.popleft()
            depth = max(depth,level)
    
            if node.left:
                que.append((node.left,level+1))
            if node.right:
                que.append((node.right, level+1))
        
        return depth
            
        