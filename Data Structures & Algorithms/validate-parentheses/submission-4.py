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
                
                if not stack or stack.pop() != brackets_dict[elem]:
                    return False


            else:
                stack.append(elem)
        

        
        return True if not stack else False

        