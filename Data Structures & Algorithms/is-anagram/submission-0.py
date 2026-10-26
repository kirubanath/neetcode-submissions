class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = {}
        t_dict = {}
        for elem in s:
            if elem in s_dict:
                s_dict[elem]+=1
            else:
                s_dict[elem]=1
        
        for elem in t:
            if elem in t_dict:
                t_dict[elem]+=1
            else:
                t_dict[elem]=1
        

        return s_dict == t_dict
                 