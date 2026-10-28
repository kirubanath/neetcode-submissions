class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0 for _ in range(9)]
        columns = [0 for _ in range(9)]
        boxes = [0 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                elem = board[i][j]

                if elem == ".":
                    continue

                bit =  1 << int(elem) 
                b = i//3*3 + j//3

                if rows[i] & bit or columns[j] & bit or boxes[b] & bit:
                    return False

                rows[i] |= bit
                columns[j] |= bit
                boxes[b] |= bit
        
        return True

