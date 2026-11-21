"""
Same as rob 1 : Just either house 1 and not last or last and not house 1
"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        # check houses 1->n-1
        max_cur1 = max_prev1 = nums[0]
        max_prev2 = 0

        for i in range(1,len(nums)-1):
            rob = nums[i] + max_prev2
            dont_rob = max_prev1
            max_cur1 = max(rob,dont_rob)
            max_prev1,max_prev2 = max_cur1,max_prev1


        # check houses 2 ->n
        max_cur2 = max_prev1 = nums[1]
        max_prev2 = 0

        for i in range(2,len(nums)):
            rob = nums[i] + max_prev2
            dont_rob = max_prev1
            max_cur2 = max(rob,dont_rob)
            max_prev1,max_prev2 = max_cur2,max_prev1


        # max of these two

        return max(max_cur1, max_cur2)