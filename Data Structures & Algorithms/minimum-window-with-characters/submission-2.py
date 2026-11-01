# Idea 
# 1. Right expand till it fits
# 2. Trim from left till it breaks
# 3. Continue!
# 4. For match just incrememntally check the count not compare the whole dic
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t)>len(s):
            return ""

        from collections import Counter
        
        # Hash map of t
        tf = Counter(t)

        # Hash map of window
        window = Counter()

        # Incremental Match variables
        have = 0
        need = len(tf) 

        res = [-1,-1]
        cur_min_length = float("infinity")

        l =0
        for r in range(len(s)):
            ch = s[r]
            window[ch]+=1

           

            # check and update have
            if ch in tf and window[ch] == tf[ch]:
                have+=1
            

            # Trim left till it breaks
            while have == need:

                #First update the result
                if r-l+1 < cur_min_length:
                    res = [l,r]
                    cur_min_length = r-l+1
                
                # Update the window map
                window[s[l]] -=1

                # Check and update have
                if s[l] in tf and window[s[l]] < tf[s[l]]:
                    have -=1

                l+=1
        

        l,r = res

        return s[l:r+1]
                




        