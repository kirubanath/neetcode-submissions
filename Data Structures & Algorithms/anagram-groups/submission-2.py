"""
Instead of sorting a string, use frequency for hash map
"""
class Solution:
    def freq_map(self,s):

        res = [0]*26

        for elem in s:
            index = ord(elem) - ord("a")
            res[index]+=1
        
        return tuple(res)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = defaultdict(list)

        for s in strs:
            mp[self.freq_map(s)].append(s)
        
        return list(mp.values())
        