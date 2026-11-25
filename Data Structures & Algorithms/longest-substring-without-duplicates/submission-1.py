class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        

        mp = defaultdict(int)
        longest = 0

        l,r = 0,0

        while r < len(s):

            # add r:
            elem = s[r]
            mp[elem]+=1

            # remove l till we satisfy:
            while mp[elem] > 1:

                mp[s[l]]-=1
                l+=1 

            # update longest:
            longest = max(longest, r-l+1)

            # increment r for next turn:
            r+=1
        
        return longest
            



        



