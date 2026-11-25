class Solution:
    def helper(self,nums): # the normal house robber

        max_prev1 = max_cur = nums[0]
        max_prev2 = 0

        for i in range(1, len(nums)):

            rob = max_prev2 +nums[i]
            drob = max_prev1

            max_cur = max(rob, drob)
            max_prev1, max_prev2 = max_cur, max_prev1
        
        return max_cur
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
        


        