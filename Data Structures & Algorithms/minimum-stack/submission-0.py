class MinStack:

    def __init__(self):
        self.stack     = []
        self.cur_count = 0
        self.min_dic   = {0 : float("inf")} 
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.cur_count+=1
        self.min_dic[self.cur_count] = min(val,self.min_dic[self.cur_count-1] )
        
    
    def pop(self) -> None:
        self.cur_count -=1
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_dic[self.cur_count]
        
