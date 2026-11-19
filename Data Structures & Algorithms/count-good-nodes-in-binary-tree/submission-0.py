# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 

        stack = [(root,float("-inf"))]
        happy = 0

        while stack:

            node,prev_max = stack.pop()

            if prev_max <= node.val:
                happy+=1
            cur_max = max(node.val,prev_max)

            if node.left:
                stack.append((node.left,cur_max))
            
            if node.right:
                stack.append((node.right, cur_max))
        

        return happy



        