"""
Every house its a simple decision of rob or dont rob
"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) ==1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0],nums[1])

        dp = [nums[0], max(nums[0],nums[1])]

        for i in range(2,len(nums)):

            # rob
            rob = nums[i] + dp[i-2]
            print(rob)

            # dont rob
            drob = dp[i-1]
            print(drob)

            dp.append(max(rob, drob))

            print(dp)
        
        return dp[-1]


        