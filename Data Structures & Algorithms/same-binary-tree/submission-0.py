# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Any BFS or DFS rep of a tree and then compare
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def tree_rep(root):
            if not root:
                return []
            
            tree = []
            que  = deque([root])

            while que:
                node = que.popleft()

                if not node:
                    tree.append("None")
                    continue
                
                tree.append(node.val)

                que.append(node.left)
                que.append(node.right)

            return tree
        
        return tree_rep(p) == tree_rep(q)
