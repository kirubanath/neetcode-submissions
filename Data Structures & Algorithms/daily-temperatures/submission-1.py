# monotonic stack : either decreasing or increasing:
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in temperatures]
        stack = []

        for i in range(len(temperatures)):
            if not stack or temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    index = stack.pop()
                    res[index] = i-index
                stack.append(i)
                
        return res
            
            
