# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Same as solution 3 but the string matching we do with Z function!
"""
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def tree_rep(node):

            rep = ""
            stack = [node]

            while stack:
                node = stack.pop()

                if not node:
                    rep+="#"
                else:

                    rep +=f"${node.val}"
                    stack.append(node.left)
                    stack.append(node.right)
                
            return rep
        
        root_rep, sub_rep = tree_rep(root), tree_rep(subRoot)

        # Z function comparision without optimization

        overall_rep = sub_rep + "|" + root_rep
        z = [0 for _ in overall_rep]
        target = len(sub_rep)

        for i in range(1,len(z)):

            val = 0
            start = i



            # calculate fresh
            for j in range(0,len(z)-i):
                if overall_rep[j] == overall_rep[j+start]:
                    val+=1
                else:
                    break
            
            z[i] = val

            # check and return:
            if val == target:
                return True
        
        return False

        



        