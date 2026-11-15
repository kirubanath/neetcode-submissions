class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_dict = {
            ')' : '(',
            '}': '{',
            ']' : '['
        }

        for elem in s:
            if elem in brackets_dict:
                
                if not stack or (not stack.pop() == brackets_dict[elem]):
                    return False


            else:
                stack.append(elem)
        
        if not stack:
            return True
        
        return False

        