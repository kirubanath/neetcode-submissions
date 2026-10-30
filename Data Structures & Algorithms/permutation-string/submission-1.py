class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Use list as a frequency map
        f1,f2 = [0]*26, [0]*26

        if len(s1) > len(s2):
            return False
        
        # One time full map computation:
        for i in range(len(s1)):
            f1[ord(s1[i]) - ord("a")] +=1
            f2[ord(s2[i]) - ord("a")] +=1
        
        # check if its already a match
        if f1 == f2:
            return True
        
     

        # sliding window of size s1
        for r in range(len(s1),len(s2)):
            l = r - len(s1) # letter going out
            f2[ord(s2[l]) - ord("a")] -=1 
            f2[ord(s2[r]) - ord("a")] +=1 # letter coming in
            
            # compare:
            if f1 == f2:
                return True
        
        return False



        