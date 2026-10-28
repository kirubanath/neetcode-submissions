class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9) ]
        columns =[set() for _ in range(9)]
        boxes = [set() for _ in range(9)] 

        for i in range(9):
            for j in range(9):

                elem = board[i][j]

                if elem == ".":
                    continue
                
                b = i//3*3 + j//3

                if elem in rows[i] or elem in columns[j] or elem in boxes[b]:
                    return False
                
                rows[i].add(elem)
                columns[j].add(elem)
                boxes[b].add(elem)

        return True