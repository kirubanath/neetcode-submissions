"""
Combining everything : Z function with optimization
"""
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        root_str = self.tree_rep(root)
        subRoot_str = self.tree_rep(subRoot)

        # Put the pattern to match at the beginning 
        # Separator to make sure the match occurs in the root_str
        combined_str = subRoot_str + "|" + root_str 
        z = self.z_array(combined_str)

        # If any z value is same as the length of the pattern then there is a match
        return any(z[i] == len(subRoot_str) for i in range(len(combined_str)))


    def tree_rep(self, root):
        """
        Conver Tree to a string representation. 
        Value prefix : $
        None rep : #
        Use DFS not BFS
        """
        res = ""
        stack = [root]

        while stack:
            node = stack.pop()

            if not node:
                res+="#"
            
            else:
                res+=f"${node.val}"
                stack.append(node.left)
                stack.append(node.right)
        
        return res
    
    def z_array(self,s):
        """
        Slide i through 1 to n and for each position get the number of matches with the start of the string. 
        """
        n = len(s)
        
        # Init Z array
        z = [0 for _ in range(n)]

        # Init Z box
        l,r = 0,0

        for i in range(1,n):

            # Check if i is in the box:
            if i < r:

                # update with comarisions that can be safely said they are identical
                z[i] = min((r-i+1),z[i-l])

            # Start comparing and matching from next index after check above:
            while i+z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i]+=1

            # Move the box if needed:
            if i +z[i] -1 > r:
                l = i
                r = i+z[i]-1

        return z

    
        