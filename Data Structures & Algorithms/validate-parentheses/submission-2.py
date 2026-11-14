"""
Last opened must close first
"""
class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for elem in s:
            if elem in brackets:        
                if not stack or stack.pop() != brackets[elem]:
                    return False
        
            else:
                stack.append(elem)
        
        return True if not stack else False

