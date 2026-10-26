class LinkedList:
    
    def __init__(self):
        self.array = []

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.array):
            return -1
        return self.array[index]
        
    def insertHead(self, val: int) -> None:
        self.array = [val] + self.array
        

    def insertTail(self, val: int) -> None:
        self.array = self.array + [val]
        

    def remove(self, index: int) -> bool:
        if index < 0 or index >= len(self.array):
            return False
        
        if index == 0:
            self.array = self.array[1:]
        else:
            self.array = self.array[0:index] + self.array[index+1:]
        return True
        

    def getValues(self) -> List[int]:
        return self.array
        
