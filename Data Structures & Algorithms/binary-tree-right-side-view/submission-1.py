# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        que = deque([(root,0)])
        


        while que:
            node,level = que.popleft()

            if not level or level > len(res) -1:
                res.append(node.val)
            else:
                res[level] = node.val
            
            if node.left:
                que.append((node.left,level+1))
            
            if node.right:
                que.append((node.right,level+1))
            
        
        return res


