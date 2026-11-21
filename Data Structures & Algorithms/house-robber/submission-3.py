"""
Solution 1 complicated it a little bit : We said at every house there are two choices rob or dont rob and then we had to take into account what happened to the adjacent house!

But there is a simpler way:

rob or dont rob..then just get the max from remaning!

f[i] = max(rob[i] + f[i+2] , f[i+1])!! its much more simpler if we are just storing the max at every stage!
"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        profits = [nums[0]] # first house always rob will be maximum

        for i in range(1,len(nums)):

            rob = nums[i] + (profits[i-2] if i-2 >=0 else 0)
            dont_rob = profits[i-1]

            profits.append(max(rob,dont_rob))
        
        return profits[-1]
        






        