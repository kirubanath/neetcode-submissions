class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numsSet = set(nums)
        max_len = 0

        for n in nums:
            if n-1 in numsSet:
                continue

            l=1
            x=n
            while x+1 in numsSet:
                l+=1
                x+=1
            max_len = max(l,max_len)
        
        return max_len



