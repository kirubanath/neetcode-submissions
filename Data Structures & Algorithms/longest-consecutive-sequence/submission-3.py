class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = sorted(nums)
        length = 1
        max_length = 1

        for i in range(1,len(nums)):
            if s[i-1] + 1 == s[i]:
                length +=1
                max_length = max(length, max_length)
            elif s[i-1] == s[i]:
                continue
            else:
                length = 1
        
        return max_length




