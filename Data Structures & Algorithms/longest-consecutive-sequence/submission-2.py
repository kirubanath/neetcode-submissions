class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        s = set()

        for n in nums:
            if n-1 not in num_set:
                s.add(n)
        
        m_length = 1
        for start in s:
            i = start
            s_max = 1
            while i+1 in num_set:
                s_max+=1
                i+=1
            m_length = max(m_length, s_max)

        return m_length

