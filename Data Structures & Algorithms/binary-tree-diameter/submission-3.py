# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Same idea as sol2 but instead of recursion we do the stack and value maintain
Here again rather than compare with the global value, we just dynamically check the max at each node like in sol1
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        
        mp = {None : (0,0)} # map a node to its height and diameter! same as before
        stack = [root]


        while stack:

            # check if the node can be processed yet. 
            # a node can be processed when we know its left and right value
            node = stack[-1]

            if node.left and node.left not in mp: # left not processed
                stack.append(node.left)
            elif node.right and node.right not in mp: # right not processed
                stack.append(node.right)
            else:
                node = stack.pop() # We can process it now

                left_height, left_max_diam = mp[node.left]
                right_height, right_max_diam = mp[node.right]

                node_height = 1 + max(left_height, right_height)
                node_diam = left_height + right_height
                node_max_diam = max(node_diam, left_max_diam, right_max_diam)

                mp[node] = (node_height, node_max_diam)
            
        return mp[root][1]

            

                


        