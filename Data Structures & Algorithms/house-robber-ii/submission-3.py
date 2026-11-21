# cleaner way to write the solution
class Solution:
    def helper(self,nums):
        prev1,prev2 = 0,0

        for n in nums:
            new = max(n+prev2 , prev1)
            prev1, prev2 = new, prev1
        return prev1

    def rob(self, nums: List[int]) -> int:

        # rob house 1
        case1 = self.helper(nums[:-1])
        
        # dont rob house 1
        case2 = self.helper(nums[1:])

        # edge case : There is only one house
        edge_case = nums[0]

        return max(edge_case, case1, case2)

        