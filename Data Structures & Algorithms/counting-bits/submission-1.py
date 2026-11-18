class Solution:
    def countBits(self, n: int) -> List[int]:
        if not n:
            return [0]

        res = [0]
        pointer = 0
        for i in range(1,n+1):
            print(pointer, i , res)

            if i & (i-1) == 0:
                
                # reset the pointer
                pointer = 0
                res.append(1)
            
            else:
                res.append(res[pointer] + 1)
            pointer+=1
        
        return res

