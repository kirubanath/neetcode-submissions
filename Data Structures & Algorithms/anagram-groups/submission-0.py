class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # frequency of a string
        def frequency_hash(s):
            count_list = [0]*26
            for elem in s:
                count_list[ord(elem)-ord("a")]+=1
            
            return tuple(count_list)
        
        frequency_dict = {}
        for s in strs:
            s_hash = frequency_hash(s)
            if s_hash in frequency_dict:
                frequency_dict[s_hash].append(s)
            else:
                frequency_dict[s_hash] = [s]
        

        output_list = []
        for elem in frequency_dict:
            output_list.append(frequency_dict[elem])
        
        return output_list
        

        
                



        