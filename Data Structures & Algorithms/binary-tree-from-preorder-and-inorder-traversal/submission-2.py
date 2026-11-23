"""
Solution 1 TLE becuase for finding the index in indorder we are using o(n)
We can just have a hashmap and lookup
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {val:index for index,val in enumerate(inorder)}

        self.pre_idx = 0

        def dfs(l,r):
            if l > r:
                return None
            

            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx+=1

            middle = inorder_map[root.val]

            root.left = dfs(l,middle-1)
            root.right = dfs(middle+1,r)

            return root
        
        return dfs(0,len(inorder)-1)


        
            

        