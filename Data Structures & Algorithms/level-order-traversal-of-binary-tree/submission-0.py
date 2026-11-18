# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        que = deque([(root,0)])
        res = [[]]

        while que:

            node,level = que.popleft()

            while level > len(res) -1:
                res.append([])
            
            res[level].append(node.val)

            if node.left:
                que.append((node.left,level+1))
            
            if node.right:
                que.append((node.right, level+1))
            
        return res

