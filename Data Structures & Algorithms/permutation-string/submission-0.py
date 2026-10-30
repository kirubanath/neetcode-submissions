class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def freq(s):
            d = {}
            for char in s:
                d[char] = 1+ d.get(char,0)
            
            return d
        

        l = 0
        cf_s1 = freq(s1)
        for r in range(len(s1)-1,len(s2)):
            if freq(s2[l:r+1]) == cf_s1:
                return True
            
            l+=1
        
        return False





