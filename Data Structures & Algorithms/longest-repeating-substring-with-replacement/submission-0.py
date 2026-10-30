class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        cf_dict = {}
        max_len = 0

        for r in range(len(s)):

            # check and increase the frequency of the char
            cf_dict[s[r]] = 1 + cf_dict.get(s[r],0)

            # Get to a valid winow for this r -> replacements required <= k
            # total chars - max_frequency <= k
            while  (r - l + 1) - max(cf_dict.values()) > k:
                cf_dict[s[l]]-=1
                l+=1
            
            # Now that we are in the valid window get the size and move on
            max_len = max(max_len,(r-l+1))
        
        return max_len


