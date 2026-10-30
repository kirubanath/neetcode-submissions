# We can optimize by just comparing the two elements and not the entire list all the time
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False


        f1,f2 = [0]*26,[0]*26
        matches = 0

        # Consturct init maps
        for i in range(len(s1)):
            f1[ord(s1[i]) - ord("a")] +=1
            f2[ord(s2[i]) - ord("a")] +=1
           
        
        # check initial match
        for i in range(26):
            if f1[i] == f2[i]:
                matches +=1
        
        # Compare matches
        if matches == 26:
            return True
        
        
        
        
        for char_in_index in range(len(s1), len(s2)):
            char_out_index = char_in_index - len(s1)
            
            char_out = ord(s2[char_out_index])- ord("a")
            char_in  = ord(s2[char_in_index]) - ord("a")

            # instead of comparing the whole list just compare the incremental updates
            f2[char_out] -=1
            v_out = 0
            
            if f2[char_out] == f1[char_out]:
                v_out += 1
            elif f2[char_out] + 1 == f1[char_out]:
                v_out -=1

            


            f2[char_in] +=1
            v_in = 0
            if f2[char_in] == f1[char_in]:
                v_in += 1
            elif f2[char_in] -1 == f1[char_in]:
                v_in -=1
            
            

            matches = matches + v_in + v_out

            print(matches)
            if matches == 26:
                return True

        return False



