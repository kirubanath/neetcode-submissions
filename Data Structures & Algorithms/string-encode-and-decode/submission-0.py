class Solution:

    def encode(self, strs: List[str]) -> str:
        master_string = ""
        for s in strs:
            master_string+=f"{len(s)}#{s}"
        return master_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            length = ""
            while s[i]!="#" and i < len(s):
                length+=s[i]
                i+=1
            
            if i >=len(s):
                return decoded_list
            

            length = int(length)
            new_string = s[i+1:i+length+1]
            decoded_list.append(new_string)
            i=i+length+1
        
        return decoded_list






