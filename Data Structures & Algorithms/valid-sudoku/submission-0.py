class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hf = [[0 for _ in range(9)] for _ in range(9)]
        vf = [[0 for _ in range(9)] for _ in range(9)]
        bf = [[0 for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                try:
                    elem = int(board[i][j])
                

                    # check and note down in hf:
                    hf[i][elem-1] +=1
                    if hf[i][elem-1] >1:
                        return False

                    # check and note down in vf:
                    vf[j][elem-1] +=1
                    if vf[j][elem-1] >1:
                        return False
                    
                    # check and note down in bf:
                    if i < 3:
                        a = i//3 + j//3
                    elif i < 6:
                        a = 2 + i//3 + j//3
                    else:
                        a = 4 + i//3 + j//3
                    
                    bf[a][elem-1]+=1
                    if bf[a][elem-1] >1:
                        return False
                except:
                    continue
        
        return True





