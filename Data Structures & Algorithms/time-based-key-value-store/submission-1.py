class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.table:
            self.table[key].append((timestamp,value))
        else:
            self.table[key]= [(timestamp,value)]
        

    def get(self, key: str, timestamp: int) -> str:
        
        # Key itself is not present
        if key not in self.table:
            return ""

        # # no matching timestamp possible
        # if self.table[key][0][0] > timestamp:
        #     return ""


        l,r = 0, len(self.table[key]) -1
        res = ""

        
        while l <=r:

            m = (l+r)//2

            
            if self.table[key][m][0] <= timestamp:
                res = self.table[key][m][1]
                l = m+1
            
            else:
                r = m-1
        
        return res
            

        
