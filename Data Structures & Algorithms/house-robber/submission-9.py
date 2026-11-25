"""
Every house its a simple decision of rob or dont rob
"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        max_cur = max_prev1 = nums[0]
        max_prev2 = 0

        for i in range(1,len(nums)):

            rob  = nums[i] + max_prev2
            drob = max_prev1

            max_cur = max(rob, drob)

            max_prev1, max_prev2 = max_cur, max_prev1

        return max_cur 

        

        