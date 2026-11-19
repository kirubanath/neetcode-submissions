# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        que = deque([(root, float("-inf"), float("inf"))])

        while que:

            node,lb,ub = que.popleft()

            # check if the node is not valid:
            if not (lb < node.val < ub):
                return False
            
            if node.left:
                que.append((node.left,lb,node.val))
            
            if node.right:
                que.append((node.right,node.val,ub))
        
        return True
            

                 


        
        