class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_len  = 0
        start = 0

        for ch in s:
            while ch in char_set:
                char_set.remove(s[start])
                start+=1
            char_set.add(ch)
            max_len = max(max_len,len(char_set))
        
        return max_len
