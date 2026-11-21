"""
At every house there are only two choices
1. rob it
2. dont rob it

So for two adjacent houses there are three possibilities:
0,1
1,0
0,0
"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        rob_profit = [(nums[0],0)] # first house rob or dont rob

        for i in range(1,len(nums)):

            # rob:
            rob = nums[i] + rob_profit[i-1][1]

            # dont rob:
            dont_rob = 0 + max(rob_profit[i-1][0],rob_profit[i-1][1])

            # note down both cases:
            rob_profit.append((rob,dont_rob))

        return max(rob_profit[-1])
        



        